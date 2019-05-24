#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib
import json

version = "15.10"
arch = "i386" # i386 or amd64
 
mirrorlist = ["http://ubuntu.mirror.mendoza-conicet.gob.ar/", "http://releases.ubuntu.unc.edu.ar/", "http://ftp.iinet.net.au/pub/ubuntu-releases/", "http://mirror.aarnet.edu.au/pub/ubuntu/releases/", "http://mirror.netspace.net.au/pub/ubuntu-releases/", "http://ubuntu.mirror.serversaustralia.com.au/ubuntu-releases/", "http://ubuntu.mirror.uber.com.au/releases/", "http://mirror.internode.on.net/pub/ubuntu/releases/", "http://ubuntu.lagis.at/releases/", "http://mirrors.ispros.com.bd/ubuntu-release/", "http://by.releases.ubuntu.com/", "http://ubuntu-releases.mirror.nucleus.be/", "http://ubuntu.mirrors.skynet.be/pub/ubuntu.com/releases/", "http://bw.releases.ubuntu.com/", "http://ubuntu.c3sl.ufpr.br/releases/", "http://mirror.globo.com/ubuntu/releases/", "http://mirror.pop-sc.rnp.br/mirror/ubuntu/", "http://ubuntu.mirror.pop-sc.rnp.br/mirror/ubuntu-releases/", "http://mirror.unesp.br/ubuntu-releases/", "http://ubuntu-release.locaweb.com.br/", "http://ubuntu.laps.ufpa.br/releases/", "http://ubuntu.mirror.pop-sc.rnp.br/ubuntu-releases/", "http://ubuntu.ipacct.com/releases/", "http://ubuntu.linux-bg.org/releases/", "http://ubuntu-releases.mirror.nexicom.net/", "http://mirror.clibre.uqam.ca/ubuntu-releases/", "http://mirror.csclub.uwaterloo.ca/ubuntu-releases/", "http://ubuntu.bhs.mirrors.ovh.net/ftp.ubuntu.com/releases/", "http://mirror.cpsc.ucalgary.ca/mirror/ubuntu.com/releases/", "http://mirror.uchile.cl/ubuntu-releases/", "http://cl.releases.ubuntu.com/", "http://mirrors.tecnoera.com/ubuntu-releases/", "http://ftp.sjtu.edu.cn/ubuntu-cd/", "http://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/", "http://mirrors.ustc.edu.cn/ubuntu-releases/", "http://mirrors.yun-idc.com/ubuntu-releases/", "http://mirrors.zju.edu.cn/ubuntu-releases/", "http://mirror.skyshe.com/ubuntu-releases/", "http://mirrors.hust.edu.cn/ubuntu-releases/", "http://mirrors.hustunique.com/ubuntu-releases/", "http://mirrors.neusoft.edu.cn/ubuntu-releases/", "http://mirrors.oss.org.cn/ubuntuiso/", "http://ubuntu.cnssuestc.org/ubuntu-releases/", "http://mirror.edatel.net.co/ubuntu-releases/", "http://mirrors.ucr.ac.cr/ubuntu-cd/", "http://hr.releases.ubuntu.com/", "http://ucho.ignum.cz/ubuntu-releases/", "http://mirror.easyspeedy.com/ubuntu-iso/", "http://mirrors.dotsrc.org/ubuntu-cd/", "http://mirrors.telianet.dk/ubuntu-releases/", "http://ftp.estpak.ee/pub/ubuntu-releases/", "http://www.nic.funet.fi/pub/mirrors/releases.ubuntu.com/", "http://ubuntu.trumpetti.atm.tut.fi/releases/", "http://ubuntu.mirrors.proxad.net/", "http://mirror.ovh.net/ubuntu-releases/", "http://ubuntu.lafibre.info/", "http://ftp.crihan.fr/releases/", "http://ftp.oleane.net/ubuntu-cd/", "http://mirrors.ircam.fr/pub/ubuntu/releases/", "http://ubuntu.daupheus.com/", "http://ubuntu.univ-nantes.fr/ubuntu-cd/", "http://www-ftp.lip6.fr/pub/linux/distributions/Ubuntu/releases/", "http://wwwftp.ciril.fr/pub/linux/ubuntu/releases/", "http://ftp.u-picardie.fr/mirror/ubuntu/releases/", "http://distrib-coffee.ipsl.jussieu.fr/pub/linux/ubuntu-releases/", "http://mirror.skylink-datacenter.de/ubuntu-releases/", "http://ftp-stud.hs-esslingen.de/pub/Mirrors/releases.ubuntu.com/", "http://mirror2.hs-esslingen.de/releases.ubuntu.com/", "http://ubuntu.mirror.tudos.de/ubuntu-releases/", "http://ftp.fau.de/ubuntu-releases/", "http://ftp.uni-kl.de/pub/linux/ubuntu.iso/", "http://mirror.de.leaseweb.net/ubuntu-releases/", "http://mirror.informatik.uni-mannheim.de/pub/linux/distributions/ubuntu-release/", "http://mirror.serverloft.eu/ubuntu/releases/", "http://ftp.hawo.stw.uni-erlangen.de/ubuntu-releases/", "http://ftp.rrzn.uni-hannover.de/pub/mirror/linux/ubuntu-releases/", "http://ftp.uni-bayreuth.de/linux/ubuntu/releases/", "http://ftp.uni-muenster.de/pub/mirrors/ftp.ubuntu.com/releases/", "http://ftp5.gwdg.de/pub/linux/debian/ubuntu/iso/", "http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/releases/", "http://ftp.tu-clausthal.de/ftp/mirror/ubuntu/releases/", "http://ftp-stud.fht-esslingen.de/Mirrors/releases.ubuntu.com/", "http://ftp.cc.uoc.gr/mirrors/linux/ubuntu/releases/", "http://mirror.greennet.gl/releases/", "http://repo.cloudhosting.com.hk/ubuntu-releases/", "http://speglar.simnet.is/ubuntu-releases/", "http://ubuntu.excellmedia.net/releases/", "http://buaya.klas.or.id/iso/ubuntu/", "http://kartolo.sby.datautama.net.id/ubuntu-cd/", "http://mirror.unej.ac.id/pub/ubuntu-cd/", "http://linux.yazd.ac.ir/ubuntu/", "http://ftp.heanet.ie/pub/ubuntu-releases/", "http://mirror.isoc.org.il/pub/ubuntu-releases/", "http://ubuntu.interhost.co.il/", "http://releases.ubuntu.fastbull.org/ubuntu-releases/", "http://ubuntu.ictvalleumbra.it/", "http://mirror.crazynetwork.it/ubuntu/release/", "http://na.mirror.garr.it/mirrors/ubuntu-releases/", "http://ftp.jaist.ac.jp/pub/Linux/ubuntu-releases/", "http://ftp.tsukuba.wide.ad.jp/Linux/ubuntu-releases/", "http://ubuntutym2.u-toyama.ac.jp/ubuntu/", "http://ubuntu.mithril-linux.org/releases/", "http://www.ftp.ne.jp/Linux/packages/ubuntu/releases-cd/", "http://ftp.neowiz.com/ubuntu-releases/", "http://ubuntu.qualitynet.net/releases/", "http://ubuntu-rel.linux.edu.lv/", "http://ubuntu.koyanet.lv/releases/", "http://mirror.soften.ktu.lt/ubuntu-releases/", "http://ubuntu-release.mirror.serveriai.lt/", "http://ubuntu.mirror.vu.lt/releases/", "http://mirror.blizoo.mk/ubuntu-releases/", "http://archive.mmu.edu.my/ubuntu-releases/", "http://oss.mmu.edu.my/pub/ubuntu-releases/", "http://ossm.utm.my/ubuntu-DVD/", "http://ubuntu.tuxuri.com/releases/", "http://mirror.ndc.mn/ubuntu-releases/", "http://ubuntu-releases.adsolux.com/", "http://na.releases.ubuntu.com/", "http://download.polytechnic.edu.na/pub/ubuntu-release/", "http://nl.releases.ubuntu.com/releases/", "http://ftp.snt.utwente.nl/pub/os/linux/ubuntu-releases/", "http://mirror.nl.leaseweb.net/ubuntu-releases/", "http://nl3.releases.ubuntu.com/releases/", "http://ftp.snt.utwente.nl/pub/linux/ubuntu-releases/", "http://ftp.telfort.nl/pub/mirror/ubuntu-releases/", "http://ftp.tudelft.nl/releases.ubuntu.com/", "http://mirrors.nl.eu.kernel.org/ubuntu-releases/", "http://releases.ubuntu.nautile.nc/", "http://ftp.citylink.co.nz/ubuntu-releases/", "http://mirror.xnet.co.nz/pub/ubuntu-releases/", "http://mirror.ihug.co.nz/ubuntu-releases/", "http://releases.mirror.blix.com/ubuntu/", "http://ftp.uninett.no/linux/ubuntu-iso/", "http://no.releases.ubuntu.com/", "http://ubuntu.uib.no/releases/", "http://mirror.squ.edu.om/ubuntureleases/", "http://stingray.cyber.net.pk/pub/ubuntu-releases/", "http://mirror.pregi.net/pub/Linux/ubuntu-iso/", "http://ftp.icm.edu.pl/pub/Linux/ubuntu-releases/", "http://ubuntu.task.gda.pl/ubuntu-releases/", "http://ftp.vectranet.pl/ubuntu-releases/", "http://piotrkosoft.net/pub/mirrors/ubuntu-releases/", "http://cesium.di.uminho.pt/pub/ubuntu-releases/", "http://ftp.rnl.ist.utl.pt/pub/ubuntu/releases/", "http://mirrors.fe.up.pt/pub/ubuntu-releases/", "http://mirrors.nfsi.pt/ubuntu-releases/", "http://mosel.estg.ipleiria.pt/mirror/distros/ubuntu/releases/", "http://releases.ubuntumirror.dei.uc.pt/", "http://ubuntu.mirrors.linux.ro/releases/", "http://ftp.astral.ro/mirrors/ubuntu.com/releases/", "http://ftp.lug.ro/ubuntu-releases/", "http://mirror.arlug.ro/pub/ubuntu/ubuntu-releases/", "http://ftp.mtu.ru/pub/ubuntu/releases/", "http://mirror.timeweb.ru/ubuntu-releases/", "http://mirror.yandex.ru/ubuntu-releases/", "http://mirror.logol.ru/ubuntu-cd/", "http://ubuntu.saudi.net.sa/releases/", "http://ubuntu.mirrors.isu.net.sa/releases/", "http://mirror.nus.edu.sg/ubuntu-ISO/", "http://ftp.antik.sk/ubuntu-releases/", "http://tux.rainside.sk/ubuntu-releases/", "http://ubuntu.antik.sk/ubuntu-releases/", "http://ftp.wa.co.za/pub/ubuntu/releases/", "http://ubuntu.saix.net/ubuntu-releases/", "http://ubuntu.mirror.ac.za/ubuntu-release/", "http://ftp.udc.es/ubuntu-releases/", "http://ubuntu.cica.es/releases/", "http://softlibre.unizar.es/ubuntu/releases/", "http://ubuntu.uc3m.es/ubuntu-releases/", "http://ftp.caliu.cat/pub/distribucions/ubuntu/releases/", "http://ubuntu.grn.cat/ubuntu-releases/", "http://mirror.learn.ac.lk/ubuntu-releases/", "http://sz.releases.ubuntu.com/", "http://se.releases.ubuntu.com/", "http://ftp.sunet.se/pub/os/Linux/distributions/ubuntu/ubuntu-cd/", "http://ftp.availo.se/ubuntu-cd/", "http://ftp.ds.karen.hj.se/ubuntu-releases/", "http://ftp.lysator.liu.se/ubuntu-releases/", "http://ftp.portlane.com/ubuntu-releases/", "http://mirrors.se.eu.kernel.org/ubuntu-releases/", "http://mirror.switch.ch/ftp/mirror/ubuntu-cdimage/", "http://releases.ubuntu.csg.uzh.ch/ubuntu/", "http://ftp.cs.pu.edu.tw/Linux/Ubuntu/ubuntu-cd/", "http://ftp.csie.chu.edu.tw/Ubuntu/release/", "http://ftp.nsysu.edu.tw/Ubuntu/ubuntu-cd/", "http://ftp.stust.edu.tw/pub/Linux/ubuntu-cd/", "http://ftp.tc.edu.tw/iso/Ubuntu/", "http://ftp.tku.edu.tw/ubuntu-releases/", "http://ftp.twaren.net/Linux/Ubuntu/ubuntu-cd/", "http://shadow.ind.ntou.edu.tw/ubuntu-releases/", "http://ubuntu.stu.edu.tw/ubuntu-cd/", "http://mirror.kku.ac.th/ubuntu-releases/", "http://mirrors.psu.ac.th/ubuntu-releases/", "http://ubuntu-mirror.totbb.net/ubuntu-releases/", "http://ubuntu-releases.sit.kmutt.ac.th/", "http://ftp.linux.org.tr/ubuntu-releases/", "http://ftp.linux.kiev.ua/pub/Linux/Ubuntu/releases/", "http://mirrors.uaip.org/ubuntu-releases/", "http://ubuntu-releases.ip-connect.vn.ua/", "http://ubuntu.mirrorservice.org/sites/releases.ubuntu.com/", "http://mirror.as29550.net/releases.ubuntu.com/", "http://mirror.bytemark.co.uk/ubuntu-releases/", "http://mirror.ox.ac.uk/sites/releases.ubuntu.com/releases/", "http://mirror.sov.uk.goscomb.net/ubuntu-releases/", "http://mirrors.manchester.m247.com/ubuntu-releases/", "http://releases.ubuntu.mirrors.uk2.net/", "http://ftp.ticklers.org/releases.ubuntu.org/releases/", "http://mirrors.melbourne.co.uk/ubuntu-releases/", "http://releases.ubuntu.com/", "http://mirror.us.leaseweb.net/ubuntu-releases/", "http://isos.ubuntu.mirror.constant.com/", "http://mirror.lstn.net/ubuntu-releases/", "http://mirrors.advancedhosters.com/ubuntu-releases/", "http://mirrors.us.kernel.org/ubuntu-releases/", "http://ubuntu.cs.utah.edu/releases/", "http://ubuntu.osuosl.org/releases/", "http://mirrors.fwankie.com/ubuntu-releases/", "http://mirror.cogentco.com/pub/linux/ubuntu-releases/", "http://mirror.jmu.edu/pub/ubuntu-iso/", "http://mirror.metrocast.net/ubuntu-releases/", "http://mirror.nexcess.net/ubuntu-releases/", "http://mirror.symnds.com/distributions/ubuntu-releases/", "http://mirror.tcpdiag.net/ubuntu-releases/", "http://mirror.umd.edu/ubuntu-iso/", "http://mirror.uoregon.edu/ubuntu-releases/", "http://mirrors.cat.pdx.edu/ubuntu-releases/", "http://mirrors.easynews.com/linux/ubuntu-releases/", "http://mirrors.mit.edu/ubuntu-releases/", "http://mirrors.rit.edu/ubuntu-releases/", "http://reflection.oss.ou.edu/ubuntu-release/", "http://ubuntu-releases.wallawalla.edu/", "http://ubuntu.mirrors.tds.net/pub/releases/", "http://ubuntu.os6.org/", "http://ubunturelease.mirror.nac.net/", "http://ubuntu-releases.cs.umn.edu/", "http://www.gtlib.gatech.edu/pub/ubuntu-releases/", "http://cosmos.cites.illinois.edu/pub/ubuntu-iso/", "http://mirror.clarkson.edu/ubuntu-releases/", "http://mirror.hmc.edu/ubuntu-releases/", "http://ubuntu.mirror.nodebytes.com/", "http://ftp-mirror.internap.com/pub/ubuntu-releases/", "http://ftp.ucsb.edu/pub/mirrors/linux/ubuntu/", "http://mirror.cs.umn.edu/ubuntu-releases/", "http://osmirrors.cerias.purdue.edu/pub/ubuntu-releases/", "http://ubuntu.snet.uz/releases/", "http://mirrors.digipower.vn/ubuntu/releases/", "http://zw.releases.ubuntu.com/"]
activelist = []

for each_mirror in mirrorlist:
	url = each_mirror + "%s/ubuntu-%s-desktop-%s.iso" % (version, version, arch)
	try:
		request = urllib.urlopen(url)
		if request.getcode() == 404:
			pass
		else:
			activelist.append(each_mirror)
			if(activelist.__len__() == 1):
				print "1 mirror found with Ubuntu %s (%s)" % (version, arch)
				print url
				print "Search for more? (Y/N)"
				if(raw_input() != 'Y'):
					break
	except IOError:
		pass
		
json_out = json.dumps(activelist)
json_file = open('ubuntu.json', 'w')
json_file.write(json_out)
json_file.close()