from model.album import Album
from model.band import Band
from model.member import Member
from model.music import Music
from model.video import Video
from model.gig import Gig
from ycappuccino.core.api import IActivityLogger, IManager, IBootStrap, YCappuccino
import logging
from pelix.ipopo.decorators import ComponentFactory, Requires, Validate, Invalidate, Provides, Instantiate

_logger = logging.getLogger(__name__)

# init data date : 15/05/2021

@ComponentFactory('InitDataBootStrap-Factory')
@Provides(specifications=[IBootStrap.name, YCappuccino.name])
@Requires("_log", IActivityLogger.name, spec_filter="'(name=main)'")
@Requires("_manager_band", IManager.name, spec_filter="'(item_id=band)'")
@Requires("_manager_gig", IManager.name, spec_filter="'(item_id=gig)'")
@Requires("_manager_member", IManager.name, spec_filter="'(item_id=member)'")
@Requires("_manager_music", IManager.name, spec_filter="'(item_id=music)'")
@Requires("_manager_video", IManager.name, spec_filter="'(item_id=video)'")
@Requires("_manager_album", IManager.name, spec_filter="'(item_id=album)'")

@Instantiate("InitDataBootStrap")
class InitDataBootStrap(IBootStrap):

    def __init__(self):
        super(IBootStrap, self).__init__();
        self._manager_band = None
        self._manager_gig = None
        self._manager_member = None
        self._manager_music = None
        self._manager_video = None
        self._manager_album = None
        self._log = None

    def bootstrap(self):
        self._init_band()
        self._init_member()
        self._init_gig()
        self._init_music()
        self._init_video()
        self._init_album()
        self._init_gig()

    def _init_member(self):
        # y
        w_member = Member()
        w_member.id("y")
        w_member.name("Yaiba (Y)")
        w_member.role("Guitar / Vocals / Lead")
        w_member.band("yblues")
        if self._manager_member.get_one("member", w_member._id) is None:
            self._manager_member.up_sert_model(w_member._id, w_member)

        # marmotte
        w_member = Member()
        w_member.id("marmotte")
        w_member.name("Marmotte")
        w_member.role("Bass")
        w_member.band("yblues")
        if self._manager_member.get_one("member", w_member._id) is None:
            self._manager_member.up_sert_model(w_member._id, w_member)

        #spike
        w_member = Member()
        w_member.id("spike")
        w_member.name("Spike")
        w_member.role("Vocals")
        w_member.band("yblues")
        if self._manager_member.get_one("member", w_member._id) is None:
            self._manager_member.up_sert_model(w_member._id, w_member)

        #sereb
        w_member = Member()
        w_member.id("sereb")
        w_member.name("Sereb")
        w_member.role("Drums")
        w_member.band("yblues")
        if self._manager_member.get_one("member", w_member._id) is None:
            self._manager_member.up_sert_model(w_member._id, w_member)

    def _init_album(self):
        w_album = Album()
        w_album.id("arrival")
        w_album.name("The Arrival")
        w_album.producer("Y.Blues")
        w_album.release_date("30/09/2013")
        w_album.cover("img/picture/cover_arrival_petit.jpg")
        w_album.band("yblues")
        if self._manager_album.get_one("album", w_album._id) is None:
            self._manager_album.up_sert_model(w_album._id, w_album)

        w_album = Album()
        w_album.id("bttb")
        w_album.name("Belong to the Barrel")
        w_album.producer("Y.Blues")
        w_album.release_date("15/04/2017")
        w_album.cover("img/picture/cover_bttb_petit.jpg")
        w_album.band("yblues")
        if self._manager_album.get_one("album", w_album._id) is None:
            self._manager_album.up_sert_model(w_album._id, w_album)

        w_album = Album()
        w_album.id("sb")
        w_album.name("Single Barrel")
        w_album.producer("Y.Blues")
        w_album.release_date("21/03/2020")
        w_album.cover("img/picture/cover_singlebarrel_petit.jpg")

        w_album.band("yblues")
        if self._manager_album.get_one("album", w_album._id) is None:
            self._manager_album.up_sert_model(w_album._id, w_album)

    def _init_gig(self):
        w_gigs = []
        # bl1
        w_gig = Gig()
        w_gig.id("winRockFest2022")
        w_gig.name("WinteRock Fest Session#3")
        w_gig.address("")
        w_gig.city("Bonneville")
        w_gig.place("")
        w_gig.date("22/10/2022")
        w_gig.bands("Ozaru, Uutil Therapy, Primal Rage, Y.Blues, Les Crêtes Brulées")
        if self._manager_album.get_one("gig", w_gig._id) is None:
           w_gigs.append(w_gig)

        # bl1
        w_gig = Gig()
        w_gig.id("fetezik2022")
        w_gig.name("Fête de la musique")
        w_gig.address("22 Bd Gambetta, 38000 Grenoble")
        w_gig.city("Grenoble")
        w_gig.place("Le Champollion")
        w_gig.date("21/06/2022")
        w_gig.bands("Synapses, Collapse, Y.Blues, Atlasworks")
        if self._manager_album.get_one("gig", w_gig._id) is None:
            w_gigs.append(w_gig)

        w_gig = Gig()
        w_gig.id("AmperageCollabpse2022")
        w_gig.name("Amperage")
        w_gig.address("163 Cr Berriat, 38000 Grenoble")
        w_gig.city("Grenoble")
        w_gig.place("L'Amperage")
        w_gig.date("04/11/2022")
        w_gig.bands("Collapse, Y.Blues, To be announced")
        w_gigs.append(w_gig)
        if self._manager_album.get_one("gig", w_gig._id) is None:
            self._manager_gig.up_sert_many_model( w_gigs)

    def _init_music(self):
        self._init_music_arrival()
        self._init_music_bttb()
        self._init_music_sb()

    def _init_music_bttb(self):
        # arrival album
        w_musics = []
        # bl1
        w_music = Music()
        w_music.id("brokenlegsp1")
        w_music.name("Broken Legs Pt. 1")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Julien Tournoud")
        w_music.album("bttb", {"numero": 1})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Desert
        w_music = Music()
        w_music.id("desert")
        w_music.name("Desert")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Idiocrates Hinet")
        w_music.album("bttb", {"numero": 2})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Eternity
        w_music = Music()
        w_music.id("eternity")
        w_music.name("Eternity")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Spike")
        w_music.album("bttb", {"numero": 3})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # final Breath
        w_music = Music()
        w_music.id("finalbreath")
        w_music.name("Final Breath")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("bttb", {"numero": 4})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Injustice for All
        w_music = Music()
        w_music.id("injusticeforall")
        w_music.name("Injustice for All")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Bjørn Berge")
        w_music.album("bttb", {"numero": 5})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Walking man
        w_music = Music()
        w_music.id("walkingman")
        w_music.name("Walking Man")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Barefoot Iano, Madie & Spike")
        w_music.album("bttb", {"numero": 6})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Killing the Dragon Platypus
        w_music = Music()
        w_music.id("killingthedragonplatypus")
        w_music.name("Killing the Dragon Platypus (Through the Fire of My Anus)")
        w_music.composer("Yaiba")
        w_music.feat("Fetus")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("bttb", {"numero": 7})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # End of Time
        w_music = Music()
        w_music.id("endoftime")
        w_music.name("End of Time")
        w_music.composer("Yaiba")
        w_music.feat("Spike")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("bttb", {"numero": 8})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Broken Legs Pt.2
        w_music = Music()
        w_music.id("brokenlegspart2")
        w_music.name("Broken Legs Pt. 2")
        w_music.composer("Yaiba")
        w_music.feat("Emmanuelson")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("bttb", {"numero": 9})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        self._manager_music.up_sert_many_model(w_musics)

    def _init_music_sb(self):
        # arrival album
        w_musics = []
        # mind control
        w_music = Music()
        w_music.id("howmany")
        w_music.name("How Many?")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.album("sb", {"numero": 1})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # 45 reasons
        w_music = Music()
        w_music.id("45reasonsacoustic")
        w_music.name("45 Reasons")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.feat("Barefoot Iano")
        w_music.album("sb", {"numero": 2})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # app
        w_music = Music()
        w_music.id("ybluesacoustic")
        w_music.name("Y.Blues")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.feat("Barefoot Iano")
        w_music.album("sb", {"numero": 3})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # the arrival
        w_music = Music()
        w_music.id("thearrivalacoustic")
        w_music.name("The Arrival")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.album("sb", {"numero": 4})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Desert
        w_music = Music()
        w_music.id("desertacoustic")
        w_music.name("Desert")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.album("sb", {"numero": 5})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # Injustice for All
        w_music = Music()
        w_music.id("injusticeforallacoustic")
        w_music.name("Injustice for All")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.feat("Joshua")
        w_music.album("sb", {"numero": 6})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # Old N°7
        w_music = Music()
        w_music.id("oldn7acoustic")
        w_music.name("Old N°7")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("sb", {"numero": 7})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # Hailstones
        w_music = Music()
        w_music.id("hailstonesacoustic")
        w_music.name("Hailstones")
        w_music.composer("Yaiba")
        w_music.album("sb", {"numero": 8})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        self._manager_music.up_sert_many_model(w_musics)

    def _init_music_arrival(self):
        # arrival album
        w_musics =[]
        # blues savvath
        w_music = Music()
        w_music.id("bluessavvath")
        w_music.name("Blues Savvath")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 1})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        #the thing
        w_music = Music()
        w_music.id("thething")
        w_music.name("The Thing")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Benjamin Dupré")
        w_music.album("arrival",{"numero": 2})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # mind control
        w_music = Music()
        w_music.id("mindcontrol")
        w_music.name("Mind Control")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.feat("Vince")
        w_music.album("arrival",{"numero": 3})
        if self._manager_album.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # 45 reasons
        w_music = Music()
        w_music.id("45reasons")
        w_music.name("45 Reasons")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 4})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # prisoner
        w_music = Music()
        w_music.id("prisoner")
        w_music.name("Prisoner")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 5})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)

        # app
        w_music = Music()
        w_music.id("yblues")
        w_music.name("Y.Blues")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 6})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # the arrival
        w_music = Music()
        w_music.id("thearrival")
        w_music.name("The Arrival")
        w_music.author("Yaiba")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 7})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        # prologue
        w_music = Music()
        w_music.id("prologue")
        w_music.name("Prologue")
        w_music.composer("Yaiba")
        w_music.arrangment("Marmotte, Sereb")
        w_music.album("arrival",{"numero": 8})
        if self._manager_music.get_one("music", w_music._id) is None:
            w_musics.append(w_music)
        self._manager_music.up_sert_many_model(w_musics)


    def _init_video(self):
        w_videos =[]

        w_video = Video()
        w_video.id("45reasons")
        w_video.name("45 Reasons")
        w_video.music("45reasons")
        w_video.url("https://www.youtube.com/embed/9BNABYtjLR4")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("epicstringbattleforwhisky")
        w_video.name("Epic String Battle for Whisky")
        w_video.url("https://www.youtube.com/embed/fFMl31hB4NU")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("injusticeforall")
        w_video.name("Injustice for All")
        w_video.music("injusticeforall")
        w_video.url("https://www.youtube.com/embed/_vcxsC_r3pA")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)
        w_video = Video()
        w_video.id("endoftime")
        w_video.name("End of Time")
        w_video.music("endoftime")
        w_video.url("https://www.youtube.com/embed/qBnd0j6rItY")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("brokenlegspart2")
        w_video.name("Broken Legs Pt.2")
        w_video.music("brokenlegspart2")
        w_video.url("https://www.youtube.com/embed/LGiwYy-7nJQ")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("thearrival")
        w_video.name("The Arrival")
        w_video.music("thearrival")
        w_video.url("https://www.youtube.com/embed/dMChbNTV_rg")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("coverocean")
        w_video.name("Cover Ocean")
        w_video.url("https://www.youtube.com/embed/Rgz36SCXfLA")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("covertrain")
        w_video.name("Cover Train")
        w_video.url("https://www.youtube.com/embed/JiWLMsMgKgY")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("coverdarrycowlchamber")
        w_video.name("Cover Darry Cowl Chamber")
        w_video.url("https://www.youtube.com/embed/QH2mjk7jt30")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("mindcontrol")
        w_video.name("Mind Control")
        w_video.url("https://www.youtube.com/embed/3FM8urVV4WM")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("aceofspades")
        w_video.name("Ace of Spades")
        w_video.url("https://www.youtube.com/embed/QDig_XMT1a8")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)

        w_video = Video()
        w_video.id("teaseryblues")
        w_video.name("Teaser")
        w_video.url("https://www.youtube.com/embed/X8nXyU7ziss")
        if self._manager_video.get_one("video", w_video._id) is None:
            w_videos.append(w_video)
        self._manager_video.up_sert_many_model(w_videos)

    def _init_band(self):
        w_band = Band()
        w_band.id("yblues")
        w_band.name("Y.Blues")
        w_band.bio("Le Jack Blues Metal, mélange (vieilli en fût) de blues moderne au bottleneck et de metal des plus sauvage, est né lorsque les membre de Y.Blues (prononcez « Ouaille Blouze ») ont compris qu'il pouvaient faire mieux ensemble que de seulement se mettre la gueule au wiskey. Avec Yaiba à la guitare acoustique et au chant, Marmotte à la basse et Sereb à la batterie, parfois groovy, parfois bourrin et même par moment absurde, Y.Blues garanti de nombreuses émotions souvent incompatibles.")
        if self._manager_band.get_one("band", w_band._id) is None:
            self._manager_band.up_sert_model(w_band._id, w_band)

    @Validate
    def validate(self, context):
        _logger.info("AccountBootStrap validating")
        try:

            self.bootstrap()
        except Exception as e:
            _logger.error("AccountBootStrap Error {}".format(e))
            _logger.exception(e)

        _logger.info("AccountBootStrap validated")

    @Invalidate
    def invalidate(self, context):
        _logger.info("AccountBootStrap invalidating")
        try:
            pass
        except Exception as e:
            _logger.error("AccountBootStrap Error {}".format(e))
            _logger.exception(e)
        _logger.info("AccountBootStrap invalidated")
