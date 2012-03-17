%define CORE_DIR /opt/VirtualPBX
%define ASTERISK_VARLIB_HOME %{_datadir}/asterisk
Name: virtual-pbx
Summary: Voice Application Server / HostedIVR solution based on asterisk - Core files
Version: 2
Release: 1
License: EPL v1.0 / CC BY 3.0
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: Igor Okunev <igor.okunev@gmail.com>
Source0:  virtual-pbx-%{release}.tar.gz
Group:    System Environment/Services
BuildArch: noarch

Requires: mysql
Requires: mysql-server
Requires: memcached
Requires: sox >= 14.3.2
Requires: ffmpeg
Requires: lame
Requires: mpg123
Requires: libmad
Requires: perl
Requires: perl(DBI)
Requires: perl(DBD::mysql)
Requires: perl(Digest::MD5)
Requires: perl(Email::Send)
Requires: perl(MIME::Lite)
Requires: perl(MIME::Types)
Requires: perl(Email::Date::Format)
Requires: perl(Cache::Memcached)
Requires: perl(Net::SSLeay)
Requires: perl(XML::SAX)
Requires: perl(Env::C)
Requires: perl(IO::Socket::SSL)
Requires: perl(Gearman::Client)
Requires: perl(Gearman::Worker)
Requires: perl(Authen::SASL)

%description
The virtual-pbx application is intended for processing incoming/outgoing calls and rapid organization IVR menu.
also provides an isolated environment (numbered plan, routing calls, institute phones and so forth. )
for multiple users.

Virtual-pbx application include:
	- Processing incoming / outgoing calls.
	- Completely isolated environment for different users 
	  ( incoming / outgoing routes, dial plan, sip-endpoints, web-interface, cdrs, call-recordings, etc ).
	- Custom user greetings support.
	- Email/Twitter notifications.
	- Multiple language voice prompts.
	- Text To Speech ( TTS ) for multiple languages.
	- Easy / Advanced configuration mode.
	- Custom music on hold (MOH) for each user.
	- Multiple language WEB interface with xml/json API support.
	- Flexible customisation for system voice messages.
	- Managing voice mail via phone or WEB interface.
	- User specified time zones support.
	- Call transfer support ( blind transfer ).
	- White / Black lists support for each IVR item.
	- Journal configuration changes.
	- CDR support.
	- IVR logging.
	- XML backup / restore configuration.
	- Multiple roles within a single IVR account.
	- Privated / Shared DIDs support.
	- SQL reports.
	- Management API.
	- Google Calendar integration.
	- Support Google Analytics for calls trekking.
	- Radius accounting.
	- Background music for Find-Me / Queue calls.
	- Support HD codec ( g722 ).
	- Email/Web interface Branding.
	- Recording outgoing calls ( auto / on demand ).
	- Full DTMF history for each call.
	- Support presettings for SIP providers.
	- Support Multi-tenant asterisk with Kamailio as sip registrar server / load balancer.
	- Easy to update.
	- speedyAGI server.
	- FMC - Fixed Mobile Convergence
	- google-chart for extended statistics for: DialOut, Queue, CallBlast, Polling
	- WEB logon / logoff for the agents of the queue.
	- Support Perl plugins.
	- Several types of extensions:
		Playback / Auto Attendant
		VoiceMail
		DialOut with Find-Me feautures.
		Company Directory
		Schedule
		WEB-Request
		Chat-Room ( with WEB broadcasting via IceCast and call recording )
		Fax2Email
		DTMF2Email
		Polling (Voting)
		DISA
		Podcast2Phone gate
		ACD Queues
		CallBack
		DateTime
		Fax on Demand
		Bulletin board system
		CallBlast ( Predictive Dialer )
		WEB Variables
		Stored DB variables
		Goto If
		Alarm Clock ( Telephone Reminder / Wake Up )
		Google Calendar - Shedule: checks status busy / free.
		RoboTEXT with support money, date, time, phonenumber, percent, degree formats
		MP3 Streaming
		Call Parking
		GoogleCalendar - Events: reads events via TTS + confirmation / cancellation of events.
		Paging / Intercom

####################################################
#
%package voip
Summary: Voice Application Server / HostedIVR solution based on asterisk - VOIP application
Group:   System Environment/Services

Requires: asterisk >= 1.6.0.28
Requires: virtual-pbx-sound-files >= 2-1_5547
Requires: virtual-pbx = %{version}-%{release}
Requires: festival
Requires: libshout
Requires: lynx
Requires: mysql-connector-odbc
Requires: unixODBC
Requires: perl(Asterisk::AGI) >= 0.09
Requires: perl(Time::HiRes)
Requires: perl(Authen::Radius)
Requires: freeradius

%description voip
Voice Application Server / HostedIVR solution based on asterisk - VOIP applications


####################################################
#
%package voip-fagi
Summary: Voice Application Server / HostedIVR solution based on asterisk - FastAGI utils
Group:   System Environment/Services

Requires: virtual-pbx-voip

%description voip-fagi
dummy package, just remove it now.

####################################################
#
%package web
Summary: Voice Application Server / HostedIVR solution based on asterisk - WEB interface
Group:   System Environment/Services

Requires: virtual-pbx = %{version}-%{release}
Requires: httpd
Requires: mod_perl
Requires: mod_ssl
Requires: perl(Apache::DBI)
Requires: perl(XML::Simple)
Requires: perl(XML::Parser)
Requires: perl(JSON::XS)
Requires: perl(CGI)

%description web
Voice Application Server / HostedIVR solution based on asterisk  - WEB interface


####################################################
#
%package management
Summary: Voice Application Server / HostedIVR solution based on asterisk - Management utilites
Group:   System Environment/Services

Requires: virtual-pbx = %{version}-%{release}
%description management
Voice Application Server / HostedIVR solution based on asterisk  - Management utilites


####################################################
#
%package sound-files
Summary: Voice Application Server / HostedIVR solution based on asterisk - Sound files
Group:   System Environment/Services

%description sound-files
Voice Application Server / HostedIVR solution based on asterisk - Sound files


####################################################
#
%package devel
Summary: Voice Application Server / HostedIVR solution based on asterisk - devel
Group:   System Environment/Services

%description devel
Voice Application Server / HostedIVR solution based on asterisk - devel


####################################################
#
%package balancer
Summary: Voice Application Server / HostedIVR solution based on asterisk - Load balancer
Group:   System Environment/Services
Requires: kamailio

%description balancer
Voice Application Server / HostedIVR solution based on asterisk - Load balancer


####################################################
#
%prep
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%setup -q -n virtual-pbx

%install
mkdir -p $RPM_BUILD_ROOT/%ASTERISK_VARLIB_HOME/sounds
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/asterisk/xvb
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.d
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.monthly
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/doc
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/db
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/recordings
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/podcasts
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/data

#start-devel
perl contrib/utils/build/proj-obf.pl
perl contrib/utils/viewlogs.pl dump project.files.sub $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/data/sub
perl contrib/utils/viewlogs.pl dump project.files.var $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/data/var
cp test-script.pl $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/
#end-devel

mv agi-bin $RPM_BUILD_ROOT/%CORE_DIR/
mv etc $RPM_BUILD_ROOT/%CORE_DIR/
mv lib $RPM_BUILD_ROOT/%CORE_DIR/
mv templates $RPM_BUILD_ROOT/%CORE_DIR/
mv web $RPM_BUILD_ROOT/%CORE_DIR/
mkdir -p $RPM_BUILD_ROOT/%CORE_DIR/web/cgi-bin
mv cgi-bin/VirtualPBX-UI.cgi $RPM_BUILD_ROOT/%CORE_DIR/web/cgi-bin/ui
mv cgi-bin/VirtualPBX-AI.cgi $RPM_BUILD_ROOT/%CORE_DIR/web/cgi-bin/ai

mv contrib/utils/podcast_get.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly/xvb-1-podcast_get.pl
mv contrib/utils/MemCached.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly/xvb-0-MemCached.pl
cp contrib/utils/db_backup.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-0-db_backup.pl
mv contrib/utils/journals_clean.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-1-journals_clean.pl
mv contrib/utils/cdr_reports.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-2-cdr_reports.pl
mv contrib/utils/cdr_clean.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-3-cdr_clean.pl
mv contrib/utils/msg_clean.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-4-msg_clean.pl
cp contrib/utils/billing_processor.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/xvb-5-billing_processor_daily.pl
mv contrib/utils/billing_processor.pl $RPM_BUILD_ROOT/%{_sysconfdir}/cron.monthly/xvb-0-billing_processor_monthly.pl
mv contrib/virtual-pbx*.cron $RPM_BUILD_ROOT/%{_sysconfdir}/cron.d/

mv contrib/utils/viewlogs.pl $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/
date > $RPM_BUILD_ROOT/%CORE_DIR/devel/%{release}/data/build-date

cp contrib/XVB.pdf $RPM_BUILD_ROOT/%CORE_DIR/web/
cp contrib/XVB-AI.pdf $RPM_BUILD_ROOT/%CORE_DIR/web/
mv contrib/XVB.pdf $RPM_BUILD_ROOT/%CORE_DIR/doc/
mv contrib/XVB.odt $RPM_BUILD_ROOT/%CORE_DIR/doc/
mv contrib/XVB-AI.pdf $RPM_BUILD_ROOT/%CORE_DIR/doc/
mv contrib/XVB-AI.odt $RPM_BUILD_ROOT/%CORE_DIR/doc/

mv contrib/fagi.rc $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/xvb-fagi
mv contrib/reg_uac.rc $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/xvb-reg_uac
mv contrib/perl-worker.rc $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/xvb-perl-worker
mv contrib/gearman-worker.rc $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/xvb-gearman-worker
mv sounds/*.tgz $RPM_BUILD_ROOT/%ASTERISK_VARLIB_HOME/sounds/
mv contrib/asterisk/extensions.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asterisk/xvb/xvb.conf
mv contrib/httpd.conf $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/xvb.conf
mv contrib/logrotate.conf $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/xvb.conf
mv contrib/BOM.txt $RPM_BUILD_ROOT/%CORE_DIR/etc/BOM-EN.txt
mv contrib/BOM-*.txt $RPM_BUILD_ROOT/%CORE_DIR/etc/
rm -f contrib/sudoers
mv contrib $RPM_BUILD_ROOT/%CORE_DIR/

mv 3rdparty $RPM_BUILD_ROOT/%CORE_DIR/

#
# clean CVS tree
#
cd $RPM_BUILD_ROOT/
find -name CVS -type d | xargs rm -rf
cd - > /dev/null

#
# template obfuscate
#
find $RPM_BUILD_ROOT/%CORE_DIR/templates -name 'voicebox_info.tt' -type f |
	while read f_name
	do
		perl $RPM_BUILD_ROOT/%CORE_DIR/contrib/utils/build/tt_preprocess.pl $f_name
	done

find $RPM_BUILD_ROOT/%CORE_DIR/templates -name 'act_extstat.tt' -type f |
	while read f_name
	do
		perl $RPM_BUILD_ROOT/%CORE_DIR/contrib/utils/build/tt_preprocess.pl $f_name
	done

export XVB_VERSION=%{release}
cd $RPM_BUILD_ROOT/%CORE_DIR/templates
find -name '*.tt' -exec perl ../contrib/utils/build/html_clean.pl {} ';'
find -name '*.bak' -exec rm -f {} ';'
ln -s xvb.RU-Male xvb.RU-Female
ln -s . default
ln -s . xvb.EN-Male
ln -s . xvb.EN-Female
ln -s . single/xvb.EN-Male
ln -s . single/xvb.EN-Female

cd - > /dev/null

#
# clean contrib/utils
#
rm -rf $RPM_BUILD_ROOT/%CORE_DIR/contrib/utils/build
rm -f $RPM_BUILD_ROOT/%CORE_DIR/contrib/Diagram.dia

#
# Unpack sounds
#
cd $RPM_BUILD_ROOT/%ASTERISK_VARLIB_HOME/sounds
find -name '*.tgz' -exec tar -xzvf {} ';'
rm $RPM_BUILD_ROOT/%ASTERISK_VARLIB_HOME/sounds/*.tgz

####################################################
#
%pre

####################################################
#
%pre voip

####################################################
#
%pre web


####################################################
#
%post
# updates
perl %CORE_DIR/contrib/utils/rpm/cfg_update.pl
perl %CORE_DIR/contrib/utils/rpm/sys_update.pl

chkconfig memcached on

####################################################
#
%post sound-files
#
# install sounds
#
find %ASTERISK_VARLIB_HOME/sounds/ -name '*.wav16' -exec perl %CORE_DIR/contrib/utils/rpm/wave-install.pl {} ';'

ln -s %ASTERISK_VARLIB_HOME/sounds/xvb.RU-Male/digits %ASTERISK_VARLIB_HOME/sounds/digits/xvb.RU-Male &> /dev/null
ln -s %ASTERISK_VARLIB_HOME/sounds/xvb.EN-Female/digits %ASTERISK_VARLIB_HOME/sounds/digits/xvb.EN-Female &> /dev/null
ln -s %ASTERISK_VARLIB_HOME/sounds/xvb.EN-Male/digits %ASTERISK_VARLIB_HOME/sounds/digits/xvb.EN-Male &> /dev/null
ln -s %ASTERISK_VARLIB_HOME/sounds/xvb.RU-Female/digits %ASTERISK_VARLIB_HOME/sounds/digits/xvb.RU-Female &> /dev/null
#
ln -s %ASTERISK_VARLIB_HOME/sounds %CORE_DIR

#
# install MOH
#
find $RPM_BUILD_ROOT/%CORE_DIR/contrib/moh -name '*.wav16' -exec perl %CORE_DIR/contrib/utils/rpm/wave-install.pl {} ';'

# fix MOH
if [ -f %{_sysconfdir}/asterisk/musiconhold.conf ]; then
	STR=`grep 'VirtualPBX' %{_sysconfdir}/asterisk/musiconhold.conf`
	if [ "x$STR" = "x" ]; then
		cat %CORE_DIR/contrib/asterisk/musiconhold.conf >> %{_sysconfdir}/asterisk/musiconhold.conf
	fi
fi

#
# install BackgroundMOH
#
find $RPM_BUILD_ROOT/%CORE_DIR/contrib/bg-moh -name '*.wav16' -exec perl %CORE_DIR/contrib/utils/rpm/wave-install.pl {} ';'
rm -rf $RPM_BUILD_ROOT/%CORE_DIR/contrib/bg-moh/by_name

####################################################
#
%post voip

# fix features
if [ -f %{_sysconfdir}/asterisk/features.conf ]; then
	STR=`grep 'VirtualPBX' %{_sysconfdir}/asterisk/features.conf`
	if [ "x$STR" = "x" ]; then
		cat %CORE_DIR/contrib/asterisk/feautures.conf >> %{_sysconfdir}/asterisk/features.conf
	fi
fi

touch /etc/asterisk/xvb/xvb-phone-service.conf || true

chkconfig asterisk on
chkconfig xvb-fagi on
chkconfig xvb-perl-worker on

STR=`LANG=C service asterisk status | grep running`
if [ "x$STR" = "x" ]; then
	service asterisk start;
else
	asterisk -rx 'dialplan reload';
	asterisk -rx 'features reload';
	# moh reload
	STR=`rpm -qv asterisk | grep '1.8'`
	if [ "x$STR" = "x" ]; then
		asterisk -rx 'moh reload';
	fi
	# perl-worker
	STR=`ps ax | grep [V]irtualPBX-perl-worker`
	if [ "x$STR" != "x" ]; then
		service xvb-perl-worker restart || killall VirtualPBX.agi || true
	fi
	# gearman-worker
	STR=`ps ax | grep [gG]earman-worker.pl`
	if [ "x$STR" != "x" ]; then
		service xvb-gearman-worker restart || killall gearman-worker.pl || true
	fi
	# reg uac
	STR=`ps ax | grep [Rr]eg_uac.pl`
	if [ "x$STR" != "x" ]; then
		service xvb-reg_uac restart || killall reg_uac.pl || true
	fi
fi

service xvb-fagi restart

####################################################
#
%post web
# apache password
touch %CORE_DIR/web/.htpasswd
# download spool init
mkdir -p /tmp/xvb-download && chmod 777 /tmp/xvb-download 

if [ -f %CORE_DIR/web/js/xvb-custom.js ]; then
	cat %CORE_DIR/web/js/xvb-custom.js >> %CORE_DIR/web/js/xvb.js
fi

chkconfig httpd on

service httpd restart


####################################################
#
%post management
#
mkdir -p /var/log/VirtualPBX/backup && chown -R asterisk.asterisk /var/log/VirtualPBX

# auto start DB
chkconfig mysqld on

# db update
perl %CORE_DIR/contrib/utils/rpm/db_update.pl

# init auth cache
perl %{_sysconfdir}/cron.hourly/xvb-0-MemCached.pl

# start services
#service memcached start
# CleanUP cache
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup tariffs
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup reports
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_TARIFF
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_CURRENCY
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_VBOX_TYPE
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_NODES
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_VBOXES_DIALOUT_TYPE
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_TZ
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_DTMF_PATTERN
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_LANG
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_VBOXES_RECORD_FTYPE
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_MOH
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_DATE_FORMAT
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_CID_TYPE
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_CID_ACTIONS
perl %CORE_DIR/contrib/utils/nodes_admin/mc_cleanup lists-VPBX_SIPPEERS_TEMPLATES

####################################################
#
%postun


####################################################
#
%files
%defattr(-,asterisk,asterisk,0750)
%attr(440,asterisk,asterisk) %config(noreplace) %CORE_DIR/etc/cid.cfg
%attr(440,asterisk,asterisk) %config(noreplace) %CORE_DIR/etc/say.cfg
%attr(440,asterisk,asterisk) %config(noreplace) %CORE_DIR/etc/xvb.cfg
%attr(440,asterisk,asterisk) %config(noreplace) %CORE_DIR/etc/locale.cfg
%attr(755,asterisk,asterisk) %config(noreplace) %CORE_DIR/etc/xvb-rc.cfg
%attr(440,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/*.conf
%attr(755,root,root) %CORE_DIR/contrib/utils/backup_restore.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/mc_view.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/check_updates.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/icecast-db-init.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/google-voice-search.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/ices2
%attr(755,root,root) %CORE_DIR/contrib/utils/rpm/*
%attr(644,root,root) %CORE_DIR/contrib/utils/rpm/sys_update-data/*
%CORE_DIR/lib/*
%CORE_DIR/templates/*
%CORE_DIR/doc/XVB.odt
%CORE_DIR/doc/XVB.pdf
%CORE_DIR/doc/XVB-AI.odt
%CORE_DIR/doc/XVB-AI.pdf
%CORE_DIR/contrib/xvb.sql
%CORE_DIR/contrib/icecast.xml
%CORE_DIR/contrib/spec-files/*.gz
%CORE_DIR/etc/BOM-*.txt


####################################################
#
%files voip
%attr(440,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/xvb/*.conf
%attr(755,root,root) %{_sysconfdir}/cron.hourly/xvb-1-podcast_get.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-4-msg_clean.pl
%attr(644,root,root) %{_sysconfdir}/cron.d/virtual-pbx-voip.cron
%attr(755,asterisk,asterisk) %CORE_DIR/agi-bin/*.agi
%attr(755,root,root) %CORE_DIR/contrib/utils/safe_xvb_perl_worker
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/xvb-perl-worker
%attr(755,root,root) %CORE_DIR/contrib/utils/safe_xvb_gearman_worker
%attr(755,root,root) %CORE_DIR/contrib/utils/gearman-worker.pl
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/xvb-gearman-worker
%attr(755,root,root) %CORE_DIR/contrib/utils/safe_xvb_reg_uac
%attr(755,root,root) %CORE_DIR/contrib/utils/reg_uac.pl
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/xvb-reg_uac
%attr(755,root,root) %CORE_DIR/contrib/utils/node_stat.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/callblast.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/xvb2astconf.pl
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/xvb-fagi
%attr(755,root,root) %CORE_DIR/contrib/utils/safe_xvb_agi
%attr(755,root,root) %CORE_DIR/contrib/utils/Fagi.pl
%CORE_DIR/contrib/asterisk/feautures.conf
%CORE_DIR/contrib/asterisk/extconfig.conf
%CORE_DIR/3rdparty/*
%CORE_DIR/contrib/odbc/*
%attr(775,asterisk,asterisk) %dir %CORE_DIR/recordings
%attr(775,asterisk,asterisk) %dir %CORE_DIR/podcasts
%attr(755,root,root) %CORE_DIR/contrib/utils/file2moh.pl

####################################################
#
%files voip-fagi


####################################################
#
%files web
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%attr(644,root,root) %{_sysconfdir}/cron.d/virtual-pbx-web.cron
%attr(755,asterisk,asterisk) %CORE_DIR/web/cgi-bin/*
%CORE_DIR/web/*
%CORE_DIR/contrib/nginx.conf


####################################################
#
%files management
%attr(644,root,root) %{_sysconfdir}/cron.d/virtual-pbx.cron
%attr(755,root,root) %{_sysconfdir}/cron.hourly/xvb-0-MemCached.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-0-db_backup.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-1-journals_clean.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-2-cdr_reports.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-3-cdr_clean.pl
%attr(755,root,root) %{_sysconfdir}/cron.daily/xvb-5-billing_processor_daily.pl
%attr(755,root,root) %{_sysconfdir}/cron.monthly/*
%attr(755,root,root) %CORE_DIR/contrib/utils/nodes_admin/*
%attr(755,root,root) %CORE_DIR/contrib/utils/queues_hourly_avg.pl
%attr(755,root,root) %CORE_DIR/contrib/utils/db_backup.pl
%attr(775,asterisk,asterisk) %dir %CORE_DIR/db


####################################################
#
%files sound-files
%ASTERISK_VARLIB_HOME/sounds
%CORE_DIR/contrib/moh/*
%CORE_DIR/contrib/bg-moh/*
%CORE_DIR/contrib/asterisk/musiconhold.conf


####################################################
#
%files devel
%attr(644,root,root) %CORE_DIR/devel/%{release}/data/*
%attr(755,root,root) %CORE_DIR/devel/%{release}/*.pl

####################################################
#
%files balancer
%attr(644,root,root) %CORE_DIR/contrib/openser/*
%changelog