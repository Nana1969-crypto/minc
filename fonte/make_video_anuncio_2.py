"""Anúncio Rouanet Urgente — vídeo 30 s, 1080x1920 (9:16), texto animado + trilha sintetizada."""
import math, random, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

W, H, FPS, DUR = 1080, 1920, 30, 17.0
NF = int(FPS * DUR)
HERE = '/tmp/claude-0/-home-user-minc/cfea5460-ff64-5d6e-92a7-67dee7b7da1d/scratchpad/video'
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/anuncio2.mp4'
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


# =============================================================== VÍDEO 2 (17 s)
BGS[:] = [
    (0.0,  bg([(540, 300, 700, (120, 30, 30), 0.35)])),
    (6.5,  bg([(540, 700, 900, (70, 30, 150), 0.60), (540, 1500, 700, GOLD, 0.10)])),
    (10.7, bg([(540, 1120, 600, GOLD, 0.10)], base=(7, 8, 13))),
    (13.5, bg([(540, 640, 650, GOLD, 0.38), (540, 1600, 800, (70, 30, 150), 0.40)])),
]

# Cena 1 — 0 a 6,4 s: o gancho (fica 6 s na tela)
add(text('A LEI ROUANET', WHITE, size=118), 540, 420, 0.00, 6.4, 'slam', 0.22)
add(text('NUNCA RECUSOU', WHITE, size=118), 540, 555, 0.25, 6.4, 'slam', 0.22)
add(text('SEU PROJETO.', WHITE, size=118), 540, 690, 0.50, 6.4, 'slam', 0.22)
add(text('VOCÊ RECUSOU', GOLD, size=128), 540, 865, 2.60, 6.4, 'slam', 0.22)
add(text('PRIMEIRO.', GOLD, size=128), 540, 1005, 2.85, 6.4, 'slam', 0.22)
small = lambda t: {'sc': 0.78}
add(folder(), 540, 1310, 0.2, 6.4, 'fade_up', 0.5, mod=small)
add(stamp('RECUSADO', RED, size=94), 540, 1325, 2.60, 6.4, 'slam', 0.16, mod=small)

# Cena 2 — 6,6 a 10,6 s: o medo ressignificado
add(text('MEDO', WHITE, size=170), 540, 500, 6.60, 10.6, 'slam', 0.24)
add(text('NÃO É DESPREPARO.', WHITE, size=96), 540, 660, 6.95, 10.6, 'slam', 0.24)
add(glow(520, GOLD, 120), 540, 920, 7.8, 10.6, 'fade', 0.8)
add(text('É SINAL DE QUE', GOLD, size=98), 540, 860, 7.90, 10.6, 'fade_up')
add(text('O PROJETO IMPORTA.', GOLD, size=98), 540, 985, 8.25, 10.6, 'fade_up')

# Cena 3 — 10,8 a 13,6 s: a porta fecha
class Door:
    """Batente dourado com a luz da fresta diminuindo até fechar (13,0 s)."""
    def __init__(self):
        self.frame = Image.new('RGBA', (560, 800), (0, 0, 0, 0))
        d = ImageDraw.Draw(self.frame)
        d.rectangle((0, 0, 559, 799), outline=GOLD + (255,), width=8)
        d.rectangle((14, 14, 545, 799), fill=(14, 16, 24, 255))
        arr = np.zeros((780, 520, 4), np.uint8)
        xs = np.linspace(-1, 1, 520)[None, :]
        arr[..., 0], arr[..., 1], arr[..., 2] = 255, 214, 140
        arr[..., 3] = (np.clip(1 - np.abs(xs) ** 1.5, 0, 1) * 255 * np.ones((780, 1))).astype(np.uint8)
        self.light = Image.fromarray(arr, 'RGBA')
        self.halo = glow(420, GOLD, 170)
    def draw(self, fr, t):
        if not (10.8 <= t < 13.6):
            return
        a = c01((t - 10.8) / 0.35) * c01((13.6 - t) / 0.2)
        k = c01((t - 11.0) / 2.0) ** 1.6                       # 0 aberta → 1 fechada
        w = int(500 * (1 - k))
        def put(img, x, y):
            if a < 0.997:
                img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * a)))
            fr.paste(img, (int(x), int(y)), img)
        if w > 2:
            hs = 0.4 + 0.6 * (1 - k)
            halo = self.halo.resize((int(840 * hs), int(840 * hs)), Image.BILINEAR)
            put(halo, 540 - halo.width / 2, 1130 - halo.height / 2)
        put(self.frame, 540 - 280, 1130 - 400)
        if w > 2:
            put(self.light.resize((w, 770), Image.BILINEAR), 540 - w / 2, 1130 - 385)
E.append(Door())
add(text('31/10', GOLD, size=220), 540, 470, 10.85, 13.6, 'slam', 0.24, 0.2)
add(text('A PORTA FECHA.', WHITE, size=104), 540, 640, 11.30, 13.6, 'fade_up', 0.35, 0.2)

# Cena 4 — 13,6 a 17 s: o produto e a chamada
cov = Image.open(COVER).convert('RGBA').resize((420, 630), Image.LANCZOS)
cm = Image.new('L', cov.size, 0); ImageDraw.Draw(cm).rounded_rectangle((0, 0, 419, 629), 18, fill=255)
cov.putalpha(cm)
add(shadowed(cov, blur=26, alpha=220, off=(0, 20)), 540, 640, 13.6, 17.2, 'pop', 0.5, 0,
    mod=lambda t: {'dy': 8 * math.sin((t - 13.6) * 2.2)})
add(text('GUIA ROUANET URGENTE', WHITE, size=66), 540, 1035, 13.8, 17.2, 'fade_up', 0.35, 0)
add(text('MONTE E ENVIE EM 3 DIAS', GOLD, INTER['800'], 52), 540, 1115, 14.0, 17.2, 'fade_up', 0.35, 0)
add(rich([('R$ 37', GOLD), ('  ·  até 31/10', WHITE)], ARCHIVO, 76), 540, 1225, 14.2, 17.2, 'slam', 0.22, 0)
add(button('SAIBA MAIS'), 540, 1375, 14.5, 17.2, 'pop', 0.4, 0,
    mod=lambda t: {'sc': 1 + 0.035 * max(0, math.sin((t - 14.9) * 6.0))})
add(text('Guia de organização. Não garante aprovação nem captação.', GREY, INTER['400'], 28), 540, 1495, 14.8, 17.2, 'fade', 0.4, 0)

SHAKES = [(0.0, 8), (0.25, 6), (0.5, 6), (2.6, 18), (6.6, 10), (10.85, 12), (13.0, 20), (14.2, 8)]
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

if __name__ == '__main__':
    if PREVIEW:
        for t in PREVIEW:
            render(int(t * FPS)).save(f'{HERE}/p2_{t:05.2f}.png')
        sys.exit()
    wav = HERE + '/trilha2.wav'
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
           '-i', '-', '-i', wav, '-c:v', 'libx264', '-preset', 'slow', '-crf', '23', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(NF):
        p.stdin.write(render(i).tobytes())
    p.stdin.close(); p.wait()
    print('ok', OUT)
