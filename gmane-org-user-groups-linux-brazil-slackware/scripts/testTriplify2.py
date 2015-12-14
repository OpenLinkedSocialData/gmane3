import  importlib, os
import multiprocessing as mp
from IPython.lib.deepreload import reload as dreload
import gmane as g, percolation as P
G=g
c=P.utils.check
importlib.reload(g.listDataStructures)
importlib.reload(g.loadMessages)
importlib.reload(g.triplifyList)
importlib.reload(P.rdf)
importlib.reload(P.utils)
importlib.reload(g.utils)
dreload(g,exclude="pytz")

#lm=g.LoadMessages("gmane.ietf.rfc822",10,basedir="~/.gmane2/")
#ds=g.ListDataStructures(lm)
#
#dl=g.DownloadGmaneData(dpath)
#dl.downloadedStats() # might take a while
dpath='/home/r/.gmane4/'
dpath='/home/r/.gmane/'
dpath='/disco/.gmane/'
load_msgs=[]
data_structs=[]
scriptpath=os.path.realpath(__file__)
fpath="./publishing/"
umbrella_dir="gmane2/"
#for list_stat in dl.lists:
#    list_id=list_stat[0]
#for list_id in ['gmane.comp.gcc.libstdc++.devel']:
#for list_id in ['gmane.comp.java.hadoop.hive.user']:
#for list_id in ['gmane.politics.organizations.metareciclagem', 'gmane.comp.gcc.libstdc++.devel', 'gmane.linux.audio.devel', 'gmane.linux.audio.users']:
#for list_id in ['gmane.comp.web.egroupware.user', 'gmane.culture.language.basque.eibartarrak','gmane.org.operators.nznog', 'gmane.science.nmr.relax.scm',"gmane.linux.fbdev.devel",]:
for list_id in ['gmane.politics.marxism.marxmail', 'gmane.mail.spam.spamassassin.devel','gmane.comp.audio.supercollider.devel',
            'gmane.linux.ubuntu.devel.kernel.general',"gmane.comp.video.ffmpeg.user","gmane.comp.mathematics.maxima.general",
        "gmane.politics.activism.neurogreen","gmane.comp.encryption.openssl.user","gmane.org.user-groups.linux.brazil.slackware",
             "gmane.comp.apache.user","gmane.comp.python.pygame",'gmane.science.linguistics.wikipedia.deutsch',
            'gmane.politics.election-methods','gmane.linux.redhat.rpm.general','gmane.comp.db.postgresql.brasil.user'][4:]:
    c(list_id)
#    lm=g.LoadMessages(list_id,basedir=dpath,n_messages=20000)
#    lm=g.LoadMessages(list_id,basedir=dpath,n_messages=200)
    lm=g.LoadMessages(list_id,basedir=dpath)
    ds=g.ListDataStructures(lm)
    foo=G.triplifyList.makeRepo(ds,fpath,dpath+list_id,"Linked data of the email list with Gmane id: {}".format(list_id),scriptpath=scriptpath,umbrella_dir=umbrella_dir)
    mm= ds.messages
    ids=ds.message_ids
    print("first: ", mm[ids[0]][2], "last:", mm[ids[-1]][2])
 
def hardClean(text):
    return "".join(c for c in text if c.isalnum() or c in allowed)
