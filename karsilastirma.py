import discord #discord kütüphanesini kodumuza çağırmış olduk.
from discord.ext import commands #botumuzun yazı yazması ,cevap vermesi için command özelliğinide import yapıyoruz.
import time #zaman komutunu eklemiş olduk
import random #rastgelelik özelliğini sağladık
import os #bilgisayaramızdaki dosyalarımıza ulaşmak için os komutunuda kodumuza ekledik.
import requests  #url almak için request komutunuda kodumuza ekledik.
intents = discord.Intents.default()#botumuza discord özelliklerini  tanımlıyoruz.
intents.message_content = True #mesajlara cevap verme özelliğini doğruluyoruz.

bot = commands.Bot(command_prefix='$', intents=intents) #botumuzun hangi işaretle başlayan girdilere cevap vereceğini belirliyoruz.

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık') #bot hazır olduğunda  botun giriş yaptığını belirtiyoruz.

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!') # $hello yazdığımızda bize cevap vermesini sağlıyoruz.

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh) #ayrıca eklediğimiz komutlardan bir tanesi

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') #ayrıca eklediğimiz komutlardan bir tanesi (kullanıcının discorda ne zaman katıldığını söylüyor.)

@bot.command()
async def repeat(ctx, times: int, content='panda'): 
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content) #belirlediğimiz kelimeyi kullanıcının girdiği değer kadar tekrarlıyor.

@bot.command()
async def yardim(ctx,times:int,content="https://support.discord.com/hc/tr\n bu link sana yardımcı olacaktır."):
    """When the user needs help this code is going to work."""
    for i in range(times):
        await ctx.send(content) # kullanıcı yardım istediğinde kullanıcıya discord destek hattının  web sitesinin linkii atıyor.

@bot.command()
async def saat(ctx):
    zaman=time.strftime(" %H:%M")
    await ctx.send(f"şuan saat:{zaman}") # $saat yazdığımızda saatin saat:dakika olarak şuan keç olduğunu söylüyor.

mod=["sen bir pandasın,Unutma!","Birinci değilsen hiçbişeysin","Gelecekteki sen, seninle gurur duyuyor.DEVAM ET!"]

@bot.command()
async def motivasyon(ctx):
  öneri=random.choice(mod)
  await ctx.send(f"Günlük motivasyon sözün:{öneri}") # motiivasyon lazım olduğunda  $motivasyon yazıyoruz ve gaza geliyoruz.


@bot.command()
async def mem(ctx):
    with open('images/resim1.png','rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) #images dosyasındaki resim1 resmini sunucuya gönderiyor.

@bot.command()
async def randommem(ctx):
    files=os.listdir("images")
    img_name=random.choice(files)
    with open(f"images/{img_name}","rb") as f:
        picture=discord.File(f)
    await ctx.send(file=picture) # $randommem yazdığımızda images listesindeki resimlerden rastgele  1 tanesini seçip  sunucuya gönderiyor.


@bot.command()
async def panda(ctx):
    dosya=os.listdir("resimler")
    rastgele_resim=random.choice(dosya)
    with open(f"resimler/{rastgele_resim}","+rb") as f:
        resim=discord.File(f)
    await ctx.send(file=resim) # $panda yazdığımızda  resimler dosyasındaki resimlerden rastgele bir tanesini seçip sunucuya gönderiyor.

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url'] 

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url) # $duck yazdığımızda bize rastgele ördek resimleri gönderiyor(başta url gözüküyor sonra resim çıkıyor.)

def get_dog_image_url():
    url2= "https://random.dog/woof.json"
    res = requests.get(url2)
    data=res.json()
    return data["url"]
"""dog komutunu çağırdığımızda bize rastgele köpek resimleri göndercek."""
@bot. command("dog")
async def dog(ctx):
    dog_url=get_dog_image_url()
    await ctx.send(dog_url) # $dog yazdığımızda bize rastgele köpek resimleri gönderiyor(başta url gözüküyor sonra resim çıkıyor.)

@bot.command()
async def cevre(ctx):
    await ctx.send("çevremizi temiz tutmamız gerektiğini biliyorsunn peki her şeyden önce  daha önemli bir soru sormamız gerek:NEDEN?\n bunun cevabını öğrenmek için $neden yazabilirsin")

neden=["1. Çevremiz temiz olmazsa her yerin pis koktuğu,çöplükle dolu bir gezegende yaşamak istemiyosan",
       "2.BU dünyada sadece senin yaşamadığını unutma"
       "3.İnsan temiz havada kendini daha iyi hisseder."]

@bot.command()
async def neden(ctx):
    cevap=random.choice(neden)
    await ctx.send(f"Buyur niye atıklarımızı geri dönüştürmemiz veya azaltmamız için 3 nedenden 1 tanesi:{neden}")

@bot.command()
async def fikir(ctx):
    fikirler=["yediğin yemekleri çöpe atmaktansa biyogübre olarak kullanabilirsin.",
             "Eğer küçükken lego oynadıysan legodan yapılabilecek birçok yeni fikir keşfedebilirsin (ör: anahtarlık,telefon tutucu vb birçok fikir bulunmakta bunun için\nhttps://youtube.com/shorts/VLR1SkV9JD4?si=-OWHZmDdYUTI_HHU videosuna bakabilirsin" ]
    cvp2=random.choice(fikirler)
    await ctx.send(f"bir fikir:{cvp2}")

















