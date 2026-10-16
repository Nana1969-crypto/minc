"""Anúncio Rouanet Urgente — vídeo 30 s, 1080x1920 (9:16), texto animado + trilha sintetizada."""
import math, random, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

W, H, FPS, DUR = 1080, 1920, 30, 30.0
NF = int(FPS * DUR)
HERE = '/tmp/claude-0/-home-user-minc/cfea5460-ff64-5d6e-92a7-67dee7b7da1d/scratchpad/video'
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/anuncio.mp4'
PREVIEW = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None

FONTS = '/home/user/minc/fonte/fonts/'
ARCHIVO = FONTS + 'archivo-black-latin-400-normal.woff2'
INTER = {w: FONTS + f'inter-latin-{w}-normal.woff2' for w in ('400', '600', '800')}
COVER = '/home/user/minc/marketing/capa-vertical-do-zero-ao-projeto-enviado.jpg'

WHITE = (245, 242, 235)
GOLD = (237, 184, 92)
RED = (229, 72, 77)
GREY = (168, 172, 186)
DARK = (13, 16, 25)

_fc = {}
def font(path, size):
    k = (path, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(path, size)
    return _fc[k]

# ---------------------------------------------------------------- easing
def c01(x): return max(0.0, min(1.0, x))
def eo3(x): x = c01(x); return 1 - (1 - x) ** 3
def eob(x, s=1.7):
    x = c01(x); c3 = s + 1
    return 1 + c3 * (x - 1) ** 3 + s * (x - 1) ** 2

# ---------------------------------------------------------------- layers
def shadowed(img, blur=14, alpha=170, off=(0, 6)):
    """Adiciona sombra suave para legibilidade."""
    pad = blur * 2 + 8
    out = Image.new('RGBA', (img.width + pad * 2, img.height + pad * 2), (0, 0, 0, 0))
    a = img.getchannel('A').point(lambda v: v * alpha // 255)
    sh = Image.new('RGBA', img.size, (0, 0, 0, 255)); sh.putalpha(a)
    out.paste(sh, (pad + off[0], pad + off[1]), sh)
    out = out.filter(ImageFilter.GaussianBlur(blur))
    out.paste(img, (pad, pad), img)
    return out

def rich(segments, path, size, max_w=960, tracking=0, shadow=True):
    """segments: [(texto, cor)] numa linha, encolhe a fonte até caber em max_w."""
    while True:
        f = font(path, size)
        widths = [f.getlength(t) + tracking * len(t) for t, _ in segments]
        if sum(widths) <= max_w or size <= 20:
            break
        size -= 2
    asc, desc = f.getmetrics()
    img = Image.new('RGBA', (int(sum(widths)) + 4, asc + desc + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(img); x = 2
    for (t, col), w in zip(segments, widths):
        if tracking:
            for ch in t:
                d.text((x, 2), ch, font=f, fill=col); x += f.getlength(ch) + tracking
        else:
            d.text((x, 2), t, font=f, fill=col); x += w
    return shadowed(img) if shadow else img

def text(t, col, path=ARCHIVO, size=110, **kw):
    return rich([(t, col)], path, size, **kw)

def rounded(w, h, r, fill, outline=None, width=0):
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=fill, outline=outline, width=width)
    return img

def chip(t, fg, bg, border=None, size=40, path=None, padx=34, pady=18):
    path = path or INTER['800']
    f = font(path, size); tw = f.getlength(t); asc, desc = f.getmetrics()
    w, h = int(tw + padx * 2), asc + desc + pady * 2
    img = rounded(w, h, h // 2, bg, border, 4 if border else 0)
    ImageDraw.Draw(img).text((padx, pady), t, font=f, fill=fg)
    return img

def folder(label='PROJETO CULTURAL'):
    w, h = 560, 380
    img = Image.new('RGBA', (w, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((30, 0, 230, 70), 18, fill=(166, 120, 52))           # aba
    d.rounded_rectangle((0, 40, w - 1, h + 39), 22, fill=(196, 148, 70))      # corpo
    d.rounded_rectangle((0, 40, w - 1, h + 39), 22, outline=(140, 98, 38), width=5)
    for i in range(4):                                                        # folhas
        y = 70 + i * 6
        d.line((40 + i * 4, y, w - 40 - i * 4, y), fill=(240, 232, 214), width=3)
    lf = font(INTER['800'], 34); lw = lf.getlength(label)
    d.rounded_rectangle((w / 2 - lw / 2 - 26, 150, w / 2 + lw / 2 + 26, 214), 10, fill=(250, 244, 230))
    d.text((w / 2 - lw / 2, 160), label, font=lf, fill=(60, 44, 20))
    for i in range(3):
        d.line((90, 270 + i * 34, w - 90, 270 + i * 34), fill=(166, 120, 52), width=4)
    return shadowed(img, blur=22, alpha=200, off=(0, 16))

def stamp(t, col, angle=-12, size=104):
    f = font(ARCHIVO, size); tw = f.getlength(t); asc, desc = f.getmetrics()
    w, h = int(tw + 90), asc + desc + 50
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((6, 6, w - 7, h - 7), 18, outline=col + (255,), width=12)
    d.text((45, 22), t, font=f, fill=col + (255,))
    rng = np.random.default_rng(7)                                            # textura de carimbo
    a = np.array(img.getchannel('A')).astype(np.float32)
    a *= (rng.random(a.shape) > 0.10).astype(np.float32) * 0.92
    img.putalpha(Image.fromarray(a.astype(np.uint8)))
    return img.rotate(angle, expand=True, resample=Image.BICUBIC)

def drawer():
    w, h = 820, 230
    img = Image.new('RGBA', (w, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rectangle((40, 0, w - 41, 46), fill=(8, 9, 14))                         # vão da gaveta
    for i in range(h):
        c = int(46 - 14 * i / h)
        d.line((0, 40 + i, w, 40 + i), fill=(c, c + 4, c + 14))
    d.rectangle((0, 40, w - 1, h + 39), outline=(70, 76, 96), width=4)
    d.rounded_rectangle((w / 2 - 110, 110, w / 2 + 110, 140), 15, fill=GOLD)
    return img

def glow(r, col, a=255):
    s = r * 2
    yy, xx = np.mgrid[0:s, 0:s]
    dd = np.sqrt((xx - r) ** 2 + (yy - r) ** 2) / r
    al = np.clip(1 - dd, 0, 1) ** 2 * a
    arr = np.zeros((s, s, 4), np.uint8); arr[..., :3] = col; arr[..., 3] = al.astype(np.uint8)
    return Image.fromarray(arr, 'RGBA')

def card(n, title, desc):
    w, h = 880, 210
    img = rounded(w, h, 28, (21, 25, 38, 255), GOLD + (255,), 3); d = ImageDraw.Draw(img)
    c = chip(f'DIA {n}', DARK, GOLD, size=34, padx=22, pady=10)
    img.paste(c, (36, 38), c)
    d.text((36, 102), title, font=font(ARCHIVO, 64), fill=WHITE)
    df = font(INTER['400'], 32)
    d.text((w - 36 - df.getlength(desc), 54), desc, font=df, fill=GREY)
    return shadowed(img, blur=18, alpha=160, off=(0, 10))

def button(t):
    w, h = 820, 140
    img = rounded(w, h, h // 2, GOLD + (255,)); d = ImageDraw.Draw(img)
    f = font(ARCHIVO, 60); tw = f.getlength(t); asc, desc = f.getmetrics()
    x0 = (w - tw - 70) / 2
    d.text((x0, (h - asc - desc) / 2 + 4), t, font=f, fill=DARK)
    ax = x0 + tw + 30; cy = h / 2                                              # seta desenhada
    d.line((ax, cy, ax + 44, cy), fill=DARK, width=12)
    d.polygon([(ax + 30, cy - 24), (ax + 58, cy), (ax + 30, cy + 24)], fill=DARK)
    return shadowed(img, blur=24, alpha=150, off=(0, 12))

# ---------------------------------------------------------------- fundos
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
def bg(glows, base=(10, 12, 19)):
    arr = np.zeros((H, W, 3), np.float32) + np.array(base, np.float32)
    for (cx, cy, r, col, k) in glows:
        g = np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)))[..., None] * k
        arr += g * np.array(col, np.float32)
    v = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.75)) ** 2)
    arr *= np.clip(1.15 - 0.55 * v, 0.35, 1)[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), 'RGB')

BGS = [
    (0.0,  bg([(540, 300, 700, (120, 30, 30), 0.35)])),                       # tensão (vermelho)
    (7.2,  bg([(540, 1350, 760, GOLD, 0.30), (540, 700, 900, (70, 30, 150), 0.55)])),  # revelação
    (13.0, bg([(540, 500, 800, (60, 30, 130), 0.45), (540, 1500, 700, GOLD, 0.10)])),
    (20.8, bg([(540, 700, 650, GOLD, 0.38), (540, 1600, 800, (70, 30, 150), 0.40)])),
    (26.0, bg([(540, 820, 700, GOLD, 0.30), (540, 300, 700, (70, 30, 150), 0.45)])),
]
def background(t):
    cur = BGS[0]
    for i, (ts, img) in enumerate(BGS):
        if t >= ts:
            cur = (i, img)
    i, img = cur
    if i > 0 and t - BGS[i][0] < 0.45:
        return Image.blend(BGS[i - 1][1], img, eo3((t - BGS[i][0]) / 0.45))
    return img.copy()

GRAIN = [Image.fromarray(np.random.default_rng(s).integers(0, 255, (H // 2, W // 2), dtype=np.uint8), 'L')
         .resize((W, H)) for s in range(4)]

# ---------------------------------------------------------------- linha do tempo
class El:
    def __init__(self, img, cx, cy, t0, t1, anim='fade_up', din=0.35, dout=0.25, mod=None):
        self.img, self.cx, self.cy, self.t0, self.t1 = img, cx, cy, t0, t1
        self.anim, self.din, self.dout, self.mod = anim, din, dout, mod

    def draw(self, frame, t):
        if not (self.t0 <= t < self.t1):
            return
        p = (t - self.t0) / self.din
        dx = dy = 0.0; sc = 1.0; al = 1.0
        if self.anim == 'fade_up':
            dy = 60 * (1 - eo3(p)); al = eo3(p)
        elif self.anim == 'slam':
            sc = 1.0 + 0.7 * (1 - eo3(p)); al = c01(p * 2.5)
        elif self.anim == 'pop':
            sc = 0.55 + 0.45 * eob(p); al = c01(p * 3)
        elif self.anim == 'slide':
            dx = 900 * (1 - eo3(p)); al = c01(p * 2)
        elif self.anim == 'fade':
            al = eo3(p)
        if self.dout:
            al *= c01((self.t1 - t) / self.dout)
        if self.mod:
            m = self.mod(t)
            dx += m.get('dx', 0); dy += m.get('dy', 0)
            sc *= m.get('sc', 1); al *= m.get('al', 1)
        if al <= 0.003:
            return
        img = self.img
        if abs(sc - 1) > 0.002:
            img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BILINEAR)
        if al < 0.997:
            img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * al)))
        x = int(self.cx + dx - img.width / 2); y = int(self.cy + dy - img.height / 2)
        frame.paste(img, (x, y), img)

E = []
def add(*a, **k):
    E.append(El(*a, **k))

# Cena 1 — 0 a 3,2 s: o gancho
add(text('O PROJETO', WHITE, size=124), 540, 470, 0.00, 3.15, 'slam', 0.22)
add(rich([('MAIS ', WHITE), ('RECUSADO', RED)], ARCHIVO, 124), 540, 615, 0.30, 3.15, 'slam', 0.22)
add(text('DA LEI ROUANET…', WHITE, size=124), 540, 760, 0.60, 3.15, 'slam', 0.22)

def sink(t):  # a pasta afunda na gaveta
    k = eo3((t - 5.5) / 0.9)
    return {'dy': 260 * k, 'sc': 1 - 0.25 * k, 'al': 1 - k}
add(folder(), 540, 1180, 0.0, 6.5, 'fade_up', 0.5, 0.05, mod=sink)
add(stamp('RECUSADO', RED, size=94), 540, 1200, 1.30, 6.5, 'slam', 0.16, 0.05, mod=sink)

# Cena 2 — 3,2 a 7,3 s: a virada
add(text('…É O QUE', WHITE, size=124), 540, 470, 3.20, 5.20, 'slam', 0.22)
add(text('NUNCA FOI', GOLD, size=140), 540, 620, 3.45, 5.20, 'slam', 0.22)
add(text('ENVIADO.', GOLD, size=140), 540, 780, 3.70, 5.20, 'slam', 0.22)
add(text('NÃO FOI REPROVADO.', WHITE, size=86), 540, 520, 5.30, 7.20, 'fade_up')
add(text('FICOU NA GAVETA.', GOLD, size=86), 540, 640, 5.75, 7.20, 'fade_up')
add(text('esperando você se sentir pronto', GREY, INTER['600'], 46), 540, 750, 6.20, 7.20, 'fade_up')

def drawer_mod(t):
    if t < 7.3:
        return {}
    k = eo3((t - 7.3) / 0.6)
    return {'dy': 120 * k, 'al': 1 - c01((t - 7.9) / 0.6)}
add(drawer(), 540, 1440, 4.8, 8.6, 'fade_up', 0.5, 0.05, mod=drawer_mod)
add(glow(620, GOLD, 230), 540, 1380, 7.3, 13.1, 'fade', 0.9, 0.3,
    mod=lambda t: {'sc': 0.6 + 0.6 * eo3((t - 7.3) / 1.2), 'al': 1 - 0.55 * c01((t - 8.6) / 1.0)})

# Cena 3 — 7,4 a 13,2 s: a regra
add(chip('A REGRA DE 2026', GOLD, (0, 0, 0, 0), GOLD + (255,), size=38), 540, 430, 7.6, 13.05, 'fade_up')
add(text('1º PROJETO', WHITE, size=132), 540, 590, 8.0, 13.05, 'slam', 0.24)
add(text('ATÉ R$ 200 MIL', GOLD, size=132), 540, 745, 8.4, 13.05, 'slam', 0.24)
add(text('NÃO PRECISA COMPROVAR', WHITE, size=70), 540, 920, 9.5, 13.05, 'fade_up')
add(text('ATUAÇÃO CULTURAL', WHITE, size=70), 540, 1010, 9.8, 13.05, 'fade_up')
add(text('Dispensa prevista na IN MinC nº 29/2026', GREY, INTER['400'], 38), 540, 1120, 10.6, 13.05, 'fade_up')

# Cena 4 — 13,2 a 20,9 s: o método
add(text('FALTA ORDEM.', GOLD, size=128), 540, 420, 13.25, 20.85, 'slam', 0.24)
add(text('NÃO CURRÍCULO.', WHITE, size=92), 540, 555, 13.85, 20.85, 'slam', 0.24)
add(card(1, 'CONSTRUIR', 'sua ideia vira projeto'), 540, 790, 15.2, 20.85, 'slide', 0.45)
add(card(2, 'ORGANIZAR', 'equipe, orçamento, prazos'), 540, 1040, 16.6, 20.85, 'slide', 0.45)
add(card(3, 'CADASTRAR', 'tudo pronto para o SALIC'), 540, 1290, 18.0, 20.85, 'slide', 0.45)
add(text('EM 3 DIAS', GOLD, size=64), 540, 1470, 19.2, 20.85, 'pop', 0.4)

# Cena 5 — 21,0 a 26,1 s: o produto
cov = Image.open(COVER).convert('RGBA').resize((560, 840), Image.LANCZOS)
cmask = Image.new('L', cov.size, 0); ImageDraw.Draw(cmask).rounded_rectangle((0, 0, 559, 839), 22, fill=255)
cov.putalpha(cmask)
add(glow(520, GOLD, 150), 540, 700, 21.0, 26.05, 'fade', 0.8, 0.3)
add(shadowed(cov, blur=30, alpha=220, off=(0, 24)), 540, 700, 21.0, 26.05, 'pop', 0.55, 0.3,
    mod=lambda t: {'dy': 10 * math.sin((t - 21) * 2.1), 'sc': 1 + 0.035 * c01((t - 21) / 5)})
add(text('GUIA ROUANET URGENTE', WHITE, size=66), 540, 1195, 21.6, 26.05, 'fade_up')
add(text('R$ 37', GOLD, size=130), 540, 1325, 22.4, 26.05, 'slam', 0.24)
add(chip('PRAZO: 31/10', WHITE, (190, 40, 46, 255), size=46), 540, 1465, 23.3, 26.05, 'pop', 0.4)

# Cena 6 — 26,2 a 30 s: a chamada
add(text('ZION PRODUÇÕES', GREY, INTER['600'], 28, tracking=6), 540, 315, 26.3, 30.1, 'fade', 0.5, 0)
add(text('TIRE SEU PROJETO', WHITE, size=96), 540, 440, 26.3, 30.1, 'fade_up', 0.35, 0)
add(text('DA GAVETA.', GOLD, size=112), 540, 565, 26.6, 30.1, 'fade_up', 0.35, 0)
add(folder(), 540, 860, 26.2, 30.1, 'pop', 0.4, 0)
add(stamp('ENVIADO', (46, 204, 113), angle=-10, size=100), 540, 880, 26.75, 30.1, 'slam', 0.16, 0)
add(button('COMPRAR AGORA'), 540, 1215, 27.3, 30.1, 'pop', 0.4, 0,
    mod=lambda t: {'sc': 1 + 0.035 * max(0, math.sin((t - 27.7) * 6.0))})
add(text('R$ 37 · acesso imediato · garantia de 7 dias', WHITE, INTER['600'], 36), 540, 1345, 27.6, 30.1, 'fade_up', 0.35, 0)
add(text('Guia de organização. Não garante aprovação nem captação.', GREY, INTER['400'], 28), 540, 1425, 27.9, 30.1, 'fade', 0.4, 0)

# tremores de tela (impactos)
SHAKES = [(0.0, 10), (0.30, 8), (0.60, 8), (1.30, 22), (3.45, 10), (3.70, 12), (8.0, 10), (8.4, 10),
          (13.25, 12), (21.0, 8), (22.4, 10), (26.75, 20)]
def shake(t):
    dx = dy = 0.0
    for ts, s in SHAKES:
        if 0 <= t - ts < 0.25:
            k = s * (1 - (t - ts) / 0.25)
            r = random.Random(int(t * 1000))
            dx += r.uniform(-k, k); dy += r.uniform(-k, k)
    return int(dx), int(dy)

def render(i):
    t = i / FPS
    fr = background(t)
    for e in E:
        e.draw(fr, t)
    g = GRAIN[i % 4]
    fr = Image.composite(Image.new('RGB', (W, H), (255, 255, 255)), fr, g.point(lambda v: v // 22))
    dx, dy = shake(t)
    if dx or dy:
        out = Image.new('RGB', (W, H), (6, 7, 11)); out.paste(fr, (dx, dy)); fr = out
    if t > DUR - 0.35:                                                         # fade final curto
        fr = Image.blend(fr, Image.new('RGB', (W, H), (0, 0, 0)), c01((t - (DUR - 0.35)) / 0.35) * 0.6)
    return fr

# ---------------------------------------------------------------- trilha
SR = 44100
def audio(path):
    n = int(SR * DUR); L = np.zeros(n); R = np.zeros(n)
    tt = np.arange(n) / SR
    def put(sig, at, gain=1.0, pan=0.0):
        s = int(at * SR); e = min(n, s + len(sig)); sig = sig[:e - s] * gain
        L[s:e] += sig * (1 - max(0, pan)); R[s:e] += sig * (1 + min(0, pan))
    def kick(f0=150, f1=45, dur=0.35, dec=9):
        x = np.arange(int(dur * SR)) / SR
        f = f1 + (f0 - f1) * np.exp(-x * 30)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * dec)
    rng = np.random.default_rng(3)
    def noise(dur, dec):
        x = np.arange(int(dur * SR)) / SR
        return rng.normal(0, 1, len(x)) * np.exp(-x * dec)
    def hit(big=False):
        k = kick(110 if big else 150, 35 if big else 45, 0.6 if big else 0.35, 6 if big else 9)
        nz = noise(0.25, 18 if big else 35)
        nz = np.convolve(nz, np.ones(6) / 6, 'same')
        out = np.zeros(max(len(k), len(nz))); out[:len(k)] += k; out[:len(nz)] += nz * (0.5 if big else 0.3)
        return out
    # cena 1-3: drone tenso + pulsação de coração
    m = tt < 13.2
    env = np.clip(tt / 1.5, 0, 1) * np.where(tt < 12.9, 1, np.clip((13.2 - tt) / 0.3, 0, 1))
    drone = (np.sin(2 * np.pi * 55 * tt) * 0.6 + np.sin(2 * np.pi * 82.41 * tt + 0.3) * 0.35
             + np.sin(2 * np.pi * 110.3 * tt) * 0.12) * (0.75 + 0.25 * np.sin(2 * np.pi * 0.4 * tt))
    L += drone * env * 0.16 * m; R += drone * env * 0.16 * m
    for b in np.arange(0.0, 12.9, 0.62):
        put(kick(90, 40, 0.3, 12), b, 0.30); put(kick(90, 40, 0.3, 12), b + 0.17, 0.18)
    for ts in (0.0, 0.30, 0.60, 3.20, 3.45, 3.70, 8.0, 8.4):
        put(hit(), ts, 0.55)
    put(hit(True), 1.30, 0.85)
    # subida (riser) para a virada
    rs = np.arange(int(0.9 * SR)) / SR
    riser = rng.normal(0, 1, len(rs)) * (rs / 0.9) ** 2 * 0.5 + np.sin(2 * np.pi * np.cumsum(200 + 700 * (rs / 0.9) ** 2) / SR) * (rs / 0.9) ** 2 * 0.3
    put(riser, 12.35, 0.45)
    put(hit(True), 13.25, 0.8)
    # cenas 4-6: pad confiante + batida
    bar = 60 / 112 * 4
    chords = [(220.0, 261.63, 329.63), (174.61, 220.0, 261.63), (261.63, 329.63, 392.0), (196.0, 246.94, 293.66)]
    seg = (tt >= 13.2)
    pad = np.zeros(n)
    for ci in range(int((DUR - 13.2) / bar) + 1):
        a, b = 13.2 + ci * bar, 13.2 + (ci + 1) * bar
        w = (tt >= a) & (tt < b)
        ch = chords[ci % 4]
        x = tt[w] - a
        env2 = np.clip(x / 0.25, 0, 1) * np.clip((bar - x) / 0.3, 0, 1)
        s = np.zeros(w.sum())
        for f in ch:
            for h in range(1, 6):
                s += np.sin(2 * np.pi * f * h * tt[w] + h) / (h ** 1.6)
        pad[w] = s * env2
    pad *= np.where(tt > DUR - 0.6, np.clip((DUR - tt) / 0.6, 0, 1), 1)
    L += pad * 0.07 * seg; R += np.roll(pad, 220) * 0.07 * seg
    beat = 60 / 112
    for b in np.arange(13.2 + bar / 2, DUR - 0.5, beat):
        put(kick(140, 48, 0.3, 11), b, 0.33)
        put(np.convolve(noise(0.06, 70), [1, -1], 'same'), b + beat / 2, 0.08, pan=0.3)
    put(hit(True), 21.0, 0.6); put(hit(), 22.4, 0.5); put(hit(True), 26.75, 0.85)
    mix = np.stack([L, R], 1)
    mix = np.tanh(mix * 1.2)
    mix *= 0.89 / np.abs(mix).max()
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes((mix * 32767).astype('<i2').tobytes())

if __name__ == '__main__':
    if PREVIEW:
        for t in PREVIEW:
            render(int(t * FPS)).save(f'{HERE}/prev_{t:05.2f}.png')
        sys.exit()
    wav = HERE + '/trilha.wav'; audio(wav)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
           '-i', '-', '-i', wav, '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(NF):
        p.stdin.write(render(i).tobytes())
        if i % 150 == 0:
            print('frame', i, flush=True)
    p.stdin.close(); p.wait()
    print('ok', OUT)
