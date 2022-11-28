%global _hardened_build 1

Summary: The NTP daemon and utilities
Name: ntp
Version: 4.2.8p13
Release: 3%{?dist}
# primary license (COPYRIGHT) : MIT
# kernel/sys/ppsclock.h (not used) : BSD with advertising
# include/ntif.h (not used) : BSD
# include/ntp_rfc2553.h : BSD with advertising
# lib/isc/commandline.c (not used) : BSD with advertising
# lib/isc/inet_aton.c (not used) : BSD with advertising
# lib/isc/strtoul.c (not used) : BSD with advertising
# lib/isc/unix/file.c : BSD with advertising
# lib/isc/inet_aton.c (not used) : BSD with advertising
# libntp/mktime.c : BSD with advertising
# libntp/ntp_random.c : BSD with advertising
# libntp/ntp_rfc2553.c : BSD with advertising
# libntp/adjtimex.c (not used) : BSD
# libparse/ : BSD
# ntpd/refclock_jjy.c: MIT
# ntpd/refclock_oncore.c : BEERWARE License (aka, Public Domain)
# ntpd/refclock_palisade.c : BSD with advertising
# ntpd/refclock_jupiter.c : BSD with advertising
# ntpd/refclock_mx4200.c : BSD with advertising
# ntpd/refclock_palisade.h : BSD with advertising
# sntp/libevent/ (not used) : BSD
# sntp/libopts/ (not used) : BSD or GPLv3+
License: MIT and BSD and BSD with advertising
Source0: http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-%{version}.tar.gz
Source1: ntp.conf
Source2: ntp.keys
Source4: ntpd.sysconfig
Source6: ntp.step-tickers
Source7: ntpdate.wrapper
Source8: ntp.cryptopw
Source9: ntpdate.sysconfig
Source10: ntp.dhclient
Source12: ntpd.service
Source13: ntpdate.service
Source14: ntp-wait.service
Source15: sntp.service
Source16: sntp.sysconfig

# fix building with system libopts (ntpbz #3132)
Patch1: ntp-sntp-sysexits.patch
# fix building without zlib-devel (ntpbz #3591)
Patch2: ntp-ssl-libs.patch
Patch100:  ntp.sgifixes.patch

URL: http://www.ntp.org
#BuildRequires: libcap-devel openssl-devel libedit-devel libevent-devel
#BuildRequires: pps-tools-devel autogen autogen-libopts-devel systemd
BuildRequires: gcc perl-generators perl-HTML-Parser

%{?systemd_requires}

# ntpstat was split off in 4.2.8p10-4
Recommends: ntpstat

# install timedated implementation that can control ntpd service
Recommends: timedatex

%description
The Network Time Protocol (NTP) is used to synchronize a computer's
time with another reference time source. This package includes ntpd
(a daemon which continuously adjusts system time) and utilities used
to query and configure the ntpd daemon.

Perl scripts are in the ntp-perl package, ntpdate is in the ntpdate
package and sntp is in the sntp package. The documentation in HTML
format is in the ntp-doc package.

%package perl
Summary: NTP utilities written in Perl
Requires: %{name} = %{version}-%{release}
%{?systemd_requires}
# perl introduced in 4.2.4p4-7
Obsoletes: %{name} < 4.2.4p4-7
BuildArch: noarch
%description perl
This package contains Perl scripts calc_tickadj, ntp-wait and ntptrace.
 
%package -n ntpdate
Summary: Utility to set the date and time via NTP
#Requires(pre): shadow-utils
%{?systemd_requires}

%description -n ntpdate
ntpdate is a program for retrieving the date and time from
NTP servers.

%package -n sntp
Summary: Standard Simple Network Time Protocol program
%{?systemd_requires}

%description -n sntp
sntp can be used as a SNTP client to query a NTP or SNTP server and either
display the time or set the local system's time (given suitable privilege).
It can be run as an interactive command or in a cron job.

%package doc
Summary: NTP documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
This package contains NTP documentation in HTML format.
 
%global ntpdocdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# pool.ntp.org vendor zone which will be used in ntp.conf
%if 0%{!?vendorzone:1}
%global vendorzone %(source /etc/os-release && echo ${ID}.)
%endif

%prep
%setup -q

%patch1 -p1 -b .sntp-sysexits
%patch2 -p1 -b .ssl-libs
%patch100 -p1 -b ntp.sgifixes.

# fix format and encoding of packaged documentation
sed -i 's|\r||g' html/scripts/{footer.txt,style.css}
#for f in COPYRIGHT; do
#	iconv -f iso8859-1 -t utf-8 > ${f}{_,} && touch -r ${f}{,_} && mv -f ${f}{_,}
#done

%build
sed -i 's|$CFLAGS -Wstrict-overflow|$CFLAGS|' configure sntp/configure
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow"
%configure \
	--sysconfdir=%{_sysconfdir}/ntp/crypto \
	--without-ntpsnmpd \
	--enable-all-clocks \
	--enable-parse-clocks \
	--enable-ntp-signd=%{_localstatedir}/run/ntp_signd \
	--disable-local-libopts
#    --with-locfile=redhat \

# fix default paths that are not configurable
sed -i 's|/var/db/ntp-kod|%{_localstatedir}/lib/sntp/kod|' sntp/sntp{-opts.c,.1*}
sed -i 's|/etc/ntp/drift|%{_localstatedir}/lib/ntp/drift|' \
	scripts/calc_tickadj/calc_tickadj{,.m*.in}
echo '#define KEYFILE "%{_sysconfdir}/ntp/keys"' >> ntpdate/ntpdate.h
echo '#define NTP_VAR "%{_localstatedir}/log/ntpstats/"' >> config.h

make %{?_smp_mflags}

# generate man pages from HTML documentation
sed -e 's|@PATH_PERL@|%{_bindir}/perl|' -e 's|@[^@]*_MS@|8|g' \
	< scripts/deprecated/html2man.in \
	> scripts/deprecated/html2man
#pushd
PREVWD=`pwd`
cd html
perl ../scripts/deprecated/html2man
# remove adjacent blank lines
sed -i 's/^[\t\ ]*$//;/./,/^$/!d' man/man*/*.[58]
cd $PREVWD
#popd 

%install
make DESTDIR=$RPM_BUILD_ROOT bindir=%{_sbindir} install

# install missing man pages (generated from HTML)
cp -r html/man/man8/{ntpdate,ntptime,tickadj}* $RPM_BUILD_ROOT%{_mandir}/man8

# package only selected documentation
rm -rf $RPM_BUILD_ROOT%{_docdir}
mkdir -p $RPM_BUILD_ROOT%{ntpdocdir}
cp -p COPYRIGHT ChangeLog NEWS $RPM_BUILD_ROOT%{ntpdocdir}

# prepare html documentation
find html | grep -E '\.(html|css|txt|jpg|gif)$' | grep -v '/build/\|sntp' | \
	cpio -pmd $RPM_BUILD_ROOT%{ntpdocdir}
find $RPM_BUILD_ROOT%{ntpdocdir} -type f | xargs chmod 644
find $RPM_BUILD_ROOT%{ntpdocdir} -type d | xargs chmod 755

#pushd
PREVWD=`pwd`
cd $RPM_BUILD_ROOT
mkdir -p .%{_sysconfdir}/{ntp/crypto,sysconfig,dhcp/dhclient.d} .%{_libexecdir}
mkdir -p .%{_localstatedir}/{lib/{s,}ntp,log/ntpstats} .%{_unitdir}
touch .%{_localstatedir}/lib/{ntp/drift,sntp/kod}
sed -e 's|VENDORZONE\.|%{vendorzone}|' \
	-e 's|ETCNTP|%{_sysconfdir}/ntp|' \
	-e 's|VARNTP|%{_localstatedir}/lib/ntp|' \
	< %{SOURCE1} > .%{_sysconfdir}/ntp.conf
touch -r %{SOURCE1} .%{_sysconfdir}/ntp.conf
install -p -m600 %{SOURCE2} .%{_sysconfdir}/ntp/keys
install -p -m755 %{SOURCE7} .%{_libexecdir}/ntpdate-wrapper
install -p -m644 %{SOURCE4} .%{_sysconfdir}/sysconfig/ntpd
install -p -m644 %{SOURCE9} .%{_sysconfdir}/sysconfig/ntpdate
sed -e 's|VENDORZONE\.|%{vendorzone}|' \
	< %{SOURCE6} > .%{_sysconfdir}/ntp/step-tickers
touch -r %{SOURCE6} .%{_sysconfdir}/ntp/step-tickers
sed -e 's|VENDORZONE\.|%{vendorzone}|' \
	< %{SOURCE16} > .%{_sysconfdir}/sysconfig/sntp
touch -r %{SOURCE16} .%{_sysconfdir}/sysconfig/sntp
install -p -m600 %{SOURCE8} .%{_sysconfdir}/ntp/crypto/pw
install -p -m755 %{SOURCE10} .%{_sysconfdir}/dhcp/dhclient.d/ntp.sh
install -p -m644 %{SOURCE12} .%{_unitdir}/ntpd.service
install -p -m644 %{SOURCE13} .%{_unitdir}/ntpdate.service
install -p -m644 %{SOURCE14} .%{_unitdir}/ntp-wait.service
install -p -m644 %{SOURCE15} .%{_unitdir}/sntp.service

#mkdir .%{_prefix}/lib/systemd/ntp-units.d
#echo 'ntpd.service' > .%{_prefix}/lib/systemd/ntp-units.d/60-ntpd.list
cd $PREVWD

rm -f $RPM_BUILD_ROOT/usr/sgug/share/man/man1/*
rm -f $RPM_BUILD_ROOT/.%{_unitdir}/*
#popd

#%%pre
#/usr/sbin/groupadd -g 38 ntp  2> /dev/null || :
#/usr/sbin/useradd -u 38 -g 38 -s /sbin/nologin -M -r -d %{_sysconfdir}/ntp ntp 2>/dev/null || :

#%%post
#%%systemd_post ntpd.service

#%%post -n ntpdate
#%%systemd_post ntpdate.service

#%%post -n sntp
#%%systemd_post sntp.service

#%%post perl
#%%systemd_post ntp-wait.service

#%%preun
#%%systemd_preun ntpd.service

#%%preun -n ntpdate
#%%systemd_preun ntpdate.service

#%%preun -n sntp
#%%systemd_preun sntp.service

#%%preun perl
#%%systemd_preun ntp-wait.service

#%%postun
#%%systemd_postun_with_restart ntpd.service

#%%postun -n ntpdate
#%%systemd_postun ntpdate.service

#%%postun -n sntp
#%%systemd_postun sntp.service

#%%postun perl
#%%systemd_postun ntp-wait.service

%files
%dir %{ntpdocdir}
%{ntpdocdir}/COPYRIGHT
%{ntpdocdir}/ChangeLog
%{ntpdocdir}/NEWS
%{_sbindir}/ntp-keygen
%{_sbindir}/ntpd
%{_sbindir}/ntpdc
%{_sbindir}/ntpq
%{_sbindir}/timetrim
%{_sbindir}/update-leap
#%%{_sbindir}/ntptime
%{_sbindir}/tickadj
%config(noreplace) %{_sysconfdir}/sysconfig/ntpd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ntp.conf
%dir %{_sysconfdir}/ntp
%config(noreplace) %{_sysconfdir}/ntp/keys
%dir %attr(750,root,ntp) %{_sysconfdir}/ntp/crypto
%config(noreplace) %{_sysconfdir}/ntp/crypto/pw
%dir %{_sysconfdir}/dhcp/dhclient.d
%{_sysconfdir}/dhcp/dhclient.d/ntp.sh
%dir %attr(-,ntp,ntp) %{_localstatedir}/lib/ntp
%ghost %attr(644,ntp,ntp) %{_localstatedir}/lib/ntp/drift
%dir %attr(-,ntp,ntp) %{_localstatedir}/log/ntpstats
%{_mandir}/man5/*.5*
#%%{_mandir}/man8/ntp-keygen.8*
#%%{_mandir}/man8/ntpd.8*
#%%{_mandir}/man8/ntpdc.8*
#%%{_mandir}/man8/ntpq.8*
%{_mandir}/man8/ntptime.8*
%{_mandir}/man8/tickadj.8*
#%%{_prefix}/lib/systemd/ntp-units.d/*.list
#%%{_unitdir}/ntpd.service

%files perl
%{_sbindir}/calc_tickadj
%{_sbindir}/ntp-wait
%{_sbindir}/ntptrace
#%%{_mandir}/man8/calc_tickadj.8*
#%%{_mandir}/man8/ntp-wait.8*
#%%{_mandir}/man8/ntptrace.8*
#%%{_unitdir}/ntp-wait.service
%{_datadir}/ntp

%files -n ntpdate
%doc COPYRIGHT
%config(noreplace) %{_sysconfdir}/sysconfig/ntpdate
%dir %{_sysconfdir}/ntp
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ntp/step-tickers
%{_libexecdir}/ntpdate-wrapper
%{_sbindir}/ntpdate
%{_mandir}/man8/ntpdate.8*
#%%{_unitdir}/ntpdate.service

%files -n sntp
%doc sntp/COPYRIGHT
%config(noreplace) %{_sysconfdir}/sysconfig/sntp
%{_sbindir}/sntp
#%%{_mandir}/man8/sntp.8*
%dir %{_localstatedir}/lib/sntp
%ghost %{_localstatedir}/lib/sntp/kod
#%%{_unitdir}/sntp.service

%files doc
%{ntpdocdir}/html

%changelog
* Sun Aug 23 2020  HAL <notes2@gmx.de> - 4.2.8p13-3
- initial commit, builds on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p13-2
- fix building without zlib-devel (#1711258)

* Thu Mar 07 2019 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p13-1
- update to 4.2.8p13 (CVE-2019-8936)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p12-1
- update to 4.2.8p12 (CVE-2018-12327 CVE-2018-7170)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p11-2
- update to 4.2.8p11 (CVE-2016-1549, CVE-2018-7170, CVE-2018-7182,
  CVE-2018-7183, CVE-2018-7184, CVE-2018-7185)
- use noepeer restriction in default config
- add gcc to build requirements

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p10-5
- use macro for systemd scriptlet dependencies

* Mon Dec 04 2017 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p10-4
- split ntpstat off from ntp (#1510565)
- remove obsolete dependency

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
- use ID from /etc/os-release to set pool.ntp.org vendor zone (#1443596)

* Wed Mar 22 2017 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p10-1
- update to 4.2.8p10 (CVE-2016-9042 CVE-2017-6451 CVE-2017-6458 CVE-2017-6460
  CVE-2017-6462 CVE-2017-6463 CVE-2017-6464)

* Wed Mar 15 2017 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p9-3
- replace ntpstat with shell script using ntpq
- remove broadcast/multicast examples from default config
- use pool directive in default config

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8p9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.8p9-1
- update to 4.2.8p9
- drop patches that were not accepted upstream
- remove dependency on ntpdate

* Tue Nov 22 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-43
- don't limit rate of packets from sources (CVE-2016-7426)
- don't change interface from received packets (CVE-2016-7429)
- fix calculation of root distance again (CVE-2016-7433)
- require authentication for trap commands (CVE-2016-9310)
- fix crash when reporting peer event to trappers (CVE-2016-9311)

* Mon Jul 18 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-42
- add mandatory Perl build-requires
- rebuild for new glibc

* Thu Jun 02 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-41
- don't disclose sensitive timestamps in ntpq/ntpdc responses (CVE-2015-8139)
- drop spoofed packets sooner (CVE-2016-4954)
- don't allow spoofed packets to reset associations using autokey
  (CVE-2016-4955)
- check authentication before switching broadcast interleaved mode
  (CVE-2016-4956)

* Mon May 02 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-40
- don't allow spoofed packet to enable symmetric interleaved mode
  (CVE-2016-1548)
- don't crash on duplicate address in unconfig command (CVE-2016-2516)
- check mode of new source in config command (CVE-2016-2518)
- make MAC check resilient against timing attack (CVE-2016-1550)

* Wed Apr 06 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-39
- update reference timestamp in orphan mode
- allow sources specified by IPv6 link-local address

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6p5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> 4.2.6p5-37
- Add missing service names to %%systemd_postun

* Thu Jan 21 2016 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-36
- don't accept server/peer packets with zero origin timestamp (CVE-2015-8138)
- fix crash with reslist command (CVE-2015-7977, CVE-2015-7978)
- fix infinite loop in ntpq/ntpdc (CVE-2015-8158)
- check key ID in packets authenticated with symmetric key (CVE-2015-7974)
- don't allow spoofed packets to demobilize associations (CVE-2015-7979,
  CVE-2016-1547, CVE-2016-4953)

* Tue Dec 15 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-35
- report clock state changes related to leap seconds
- allow -4/-6 on restrict lines with mask
- explain synchronised state in ntpstat man page

* Thu Oct 22 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-34
- check origin timestamp before accepting KoD RATE packet (CVE-2015-7704)
- allow only one step larger than panic threshold with -g (CVE-2015-5300)
- fix memory leak with autokey (CVE-2015-7701)
- don't crash with crafted autokey packet (CVE-2015-7691, CVE-2015-7692,
  CVE-2015-7702)
- don't crash in ntpq with crafted packet (CVE-2015-7852)
- don't mobilize passive association with crypto NAK (CVE-2015-7871)
- start ntpdate service after nss-lookup.target
- use weak dependency for timedatex on Fedora 24 and later

* Tue Aug 25 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-33
- ignore :config commands with invalid characters (CVE-2015-5146)
- fix crash with invalid logconfig command (CVE-2015-5194)
- fix crash when referencing disabled statistic type (CVE-2015-5195)
- don't allow setting driftfile and pidfile remotely (CVE-2015-7703)
- don't hang in sntp with crafted reply (CVE-2015-5219)

* Wed Jul 22 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-32
- fix resetting of leap status
- log when stepping clock for leap second or ignoring it with -x
- add option to set Differentiated Services Code Point (DSCP)
- allow different thresholds for forward and backward step
- retry joining multicast groups
- extend rawstats log

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-30
- fix generation of MD5 keys with ntp-keygen on big-endian systems
  (CVE-2015-3405)

* Wed Apr 08 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-29
- reject packets without MAC when authentication is enabled (CVE-2015-1798)
- protect symmetric associations with symmetric key against DoS attack
  (CVE-2015-1799)

* Thu Feb 26 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-28
- don't step clock for leap second with -x option (#1196635)
- allow creating all SHM segments with owner-only access
- allow symmetric keys up to 32 bytes again
- use larger RSA exponent in ntp-keygen
- fix crash in ntpq mreadvar command
- don't drop packets with source port below 123
- increase memlock limit again
- fix typos in ntpd man page
- improve documentation of restrict command

* Thu Feb 05 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-27
- validate lengths of values in extension fields (CVE-2014-9297)
- drop packets with spoofed source address ::1 (CVE-2014-9298)

* Thu Jan 29 2015 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-26
- require timedatex (#1136905)

* Fri Dec 19 2014 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-25
- don't generate weak control key for resolver (CVE-2014-9293)
- don't generate weak MD5 keys in ntp-keygen (CVE-2014-9294)
- fix buffer overflows via specially-crafted packets (CVE-2014-9295)
- don't mobilize passive association when authentication fails (CVE-2014-9296)

* Tue Nov 04 2014 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-24
- use network-online target in ntpdate and sntp services (#1116474)
- move sntp kod database to allow SELinux labeling

* Mon Aug 25 2014 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-23
- don't print exit status (#1050148)
- add nanosecond support to SHM refclock

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-21
- disable monitor in default ntp.conf
- warn when monitor can't be disabled due to limited restrict
- add conflict with systemd-timesyncd service

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-19
- update logconfig documentation for patched default (#1048249)
- remove kod from default restrict in ntp.conf (#1048196)

* Mon Dec 09 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-18
- fix calculation of root dispersion (#1037981)
- refresh peers on routing updates (#1028176)
- drop patch allowing -p and -u options to be used twice (#639101)
- remove unnecessary IPv6 restrict line from default ntp.conf
- replace hardening build flags with _hardened_build

* Mon Sep 23 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-17
- remove ControlGroup in ntpd service (#1011047)

* Thu Aug 08 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-16
- don't build ntpsnmpd
- remove workaround for failing autogen

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 4.2.6p5-15
- Install docs to %%{_pkgdocdir} where available.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.2.6p5-14
- Perl 5.18 rebuild

* Mon Jul 15 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-13
- ignore duplicate servers from dhclient
- don't use -Wstrict-overflow with -fno-strict-overflow
- buildrequire systemd-units
- remove pie test

* Thu May 02 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-12
- workaround failing autogen
- move files from /lib
- don't own ntp-units.d directory
- drop old systemd scriptlets
- fix dates in changelog

* Tue Apr 02 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-11
- avoid rereading /etc/services (#768804)
- remove ntp-wait dependency from ntpd service (#906753)
- add missing and remove unrecognized options in documentation
- update comments in some config files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-9
- compile with -fno-strict-overflow

* Wed Dec 05 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-8
- add option to set identity modulus size in ntp-keygen

* Fri Nov 23 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-7
- allow selection of cipher for private key files
- set identity modulus size in ntp-keygen
- create sntp subpackage
- add sntp service
- use system libopts
- add Wants=ntp-wait.service to ntpd service
- don't fail when /etc/sysconfig/ntpd is missing
- modify mlock and multiopts patches to use autogen
- make perl subpackage noarch

* Tue Nov 20 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-6
- bind broadcast client to new interfaces (#722690)
- decode hex encoded passwords in ntpq/ntpdc
- remove sample MD5 keys from default keys config

* Wed Oct 24 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-5
- fix crash in FIPS mode (#839280)
- use systemd macros if available (#850235)
- remove obsolete macros

* Tue Aug 07 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-4
- start ntpdate service after nss-lookup.target (#837486)
- update systemd-timedated integration (#846077)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-2
- update service file for systemd-timedated-ntp target (#816495)
- allow service to set realtime scheduler (#810801)
- drop comment enabling local driver in default config

* Tue Feb 28 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p5-1
- update to 4.2.6p5
- switch service type to forking

* Tue Feb 07 2012 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p4-3
- add default servers to step-tickers (#772389)
- enable PrivateTmp in ntpd service (#782520)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p4-1
- update to 4.2.6p4
- buildrequire pps-tools-devel
- fix errors in ntpstat found by coverity

* Sun Aug 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.2.6p3-5.1
- Rebuilt for rpm (#728707)

* Wed Jul 20 2011 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p3-5
- drop SysV init scripts (#697526, #714705)
- add ntp-wait service

* Fri May 06 2011 Bill Nottingham <notting@redhat.com> 4.2.6p3-4
- fix systemd scriplets to properly handle upgrades

* Wed Apr 06 2011 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p3-3
- pull in time-sync.target from ntpdate.service (Lennart Poettering)
- link with -Wl,-z,relro,-z,now options
- fix typo in ntpq man page (#664525)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6p3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p3-1
- update to 4.2.6p3

* Thu Nov 25 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p3-0.1.rc10
- update to 4.2.6p3-RC10
- fix system peer unmarking when unreachable
- fix broadcastdelay option
- fix automatic broadcast delay calibration
- fix ntp-keygen -V crash
- avoid unnecessary timeout in ntpdate
- drop nano patch
- convert ChangeLog to UTF-8

* Fri Oct 01 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-7
- allow -u and -p options to be used twice (#639101)

* Wed Sep 29 2010 jkeating - 4.2.6p2-6
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-5
- remove systemctl dependency for now
- suppress chkconfig output in %%post (#629285)
- generate ntp_decode(5) man page (#632300)

* Fri Aug 27 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-4
- fix default ntpdate sysconfig options (#445229)

* Thu Aug 26 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-3
- update ntpdate service (#627395)

* Mon Aug 23 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-2
- add support for systemd (#617328)
- retry few times in ntpdate init script before giving up (#445229)
- add fourth pool server to default ntp.conf and use iburst

* Tue Jul 13 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p2-1
- update to 4.2.6p2
- add COPYRIGHT to ntpdate subpackage

* Thu May 13 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p1-2
- update ntpstat to use current system variable names (#588067)
- print synchronization distance instead of dispersion in ntpstat
- clarify ntpd -q description

* Mon Apr 12 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p1-1
- update to 4.2.6p1

* Fri Mar 19 2010 Miroslav Lichvar <mlichvar@redhat.com> 4.2.6p1-0.1.rc5
- update to 4.2.6p1-RC5
- support NTPSERVERARGS variable in dhclient script (#558110)
- don't use deprecated egrep (#548182)
- don't verify ntp.conf (#481151)
- compile with PPS API support
- include new sntp

* Wed Dec 09 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p8-1
- update to 4.2.4p8 (#545557, CVE-2009-3563)

* Wed Oct 21 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p7-7
- add ntp-wait man page (#526161)
- fix init scripts (#527987)

* Tue Sep 29 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p7-6
- generate tickadj man page (#526161)
- fix precision calculation on fast CPUs

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.2.4p7-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4p7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p7-3
- handle system time jumps better
- don't wake up every second for refclocks without timer
- don't crash in ntpstat when unknown clock type is received (#505564)
- make ntpstat process first packet in multipacket response
- switch to editline
- set pool.ntp.org vendor zone in spec (#512711)
- compile with -fno-strict-aliasing
 
* Thu May 28 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p7-2
- fix frequency calculation when starting with no drift file
- reduce phase adjustments beyond Allan intercept in daemon PLL

* Tue May 19 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p7-1
- update to 4.2.4p7 (CVE-2009-1252)
- improve PLL response when kernel discipline is disabled
- don't log STA_MODE changes
- enable nanokernel support
- allow minpoll 3
- increase memlock limit
- move html documentation to -doc subpackage (#492444)

* Mon Apr 20 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p6-4
- don't restart ntpd in dhclient script with every renewal
- fix buffer overflow in ntpq (#490617)
- check status in condrestart (#481261)
- don't crash when compiled with HAVE_TIMER_CREATE (#486217)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4p6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p6-2
- rebuild for new openssl

* Wed Jan 14 2009 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p6-1
- update to 4.2.4p6 (CVE-2009-0021)
- include dhclient script (David Cantrell)
- convert COPYRIGHT to UTF-8

* Wed Oct 08 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p5-2
- retry failed name resolution few times before giving up (#460561)
- don't write drift file upon exit
- run ntpq with full path in ntp-wait script

* Fri Aug 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p5-1
- update to 4.2.4p5
- add support for fast interface updates

* Mon Jul 28 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-7
- reload resolv.conf after temporary failure in name resolution (#456743)
- use clock_gettime
- make subpackages for perl scripts and ntpdate (#452097, #456116)

* Mon Apr 07 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-6
- don't use /etc/sysconfig/clock in ntpdate init script

* Mon Mar 10 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-5
- fix building IPv6 support with new glibc-headers (#436713)
- avoid unaligned memory access (#435301)
- fix receiving broadcasts on 255.255.255.255

* Fri Feb 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-4
- reset kernel frequency when -x option is used
- create separate init script for ntpdate
- add note about paths and exit codes to ntpd man page

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.2.4p4-3
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-2
- rebuild for openssl bump

* Fri Oct 26 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p4-1
- update to 4.2.4p4
- fix default NTP version for outgoing packets in ntpdate man page
  (#245408)
- replace BSD with advertising code in ntpdc and ntpq

* Mon Sep 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p2-6
- require perl (#274771)
- don't fail when starting with no interfaces (#300371)

* Tue Aug 21 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p2-5
- avoid use of uninitialized floating-point values in clock_select
- update license tag (Tom "spot" Callaway)
- drop sntp, MSNTP license is non-free

* Mon Aug 13 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p2-4
- allow loopback to share non-loopback address (#249226)
- require readline >= 5.2-3 (#250917)

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 4.2.4p2-3
- Rebuild for RH #249435

* Tue Jul 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p2-2
- ignore tentative addresses (#246297)
- improve init script (#247003)
- fix sleep patch
- ease Autokey setup (#139673)
  - change default keysdir to /etc/ntp/crypto
  - set crypto password in /etc/ntp/crypto/pw
  - don't use randfile if /dev/urandom is used by OpenSSL
- change default statsdir to /var/log/ntpstats/, use statistics type
  as default filename
- package more doc files

* Thu Jun 21 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p2-1
- update to 4.2.4p2

* Tue May 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p0-3
- fix interface updates with -I or -L option (#240254)
- accept multiple -I options
- fix broadcast client/server to accept/allow sending
  broadcasts on 255.255.255.255 (#226958)
- fix return codes in init script (#240120)
- exit with nonzero code if ntpd -q did not set clock (#240134)
- drop revert452 patch, fixed in kernel 2.6.19
- make with _smp_mflags

* Wed May 09 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p0-2
- compile with crypto support on 64bit architectures (#239576)
- update sleep patch

* Wed Mar 07 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4p0-1
- update to 4.2.4p0
- fix init script
  - don't add second -g to ntpd options (#228424)
  - update getopts
  - skip all refclocks when parsing ntp.conf
- spec cleanup

* Mon Jan 29 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4-4
- don't wake up every second (#204748)
- add option to enable memory locking (#195617)
- fix broadcast client
- use option values in ntp-keygen
- improve man pages

* Tue Jan 23 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4-3
- disable autoopts option preset mechanisms for ntpd
- document -I option of ntpd
- generate makewhatis friendly man pages

* Mon Jan 08 2007 Miroslav Lichvar <mlichvar@redhat.com> 4.2.4-1
- update to 4.2.4 (#146884)
- don't use local clock in default config
- autogenerate man pages from HTML
- clean up spec a bit

* Wed Nov 22 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2p4-2
- pass additional options to ntpdate (#202204)

* Tue Nov 21 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2p4-1
- update to 4.2.2p4
- fix buffer overflow in WWV Audio driver (#216309)
- don't mark init script as config

* Fri Aug 18 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2p1-3
- use adjtime when offset is more than 0.5s (#154625)

* Mon Jul 24 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2p1-2
- link ntpd with -ffast-math on ia64 (#147980)

* Tue Jul 18 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2p1-1
- update to 4.2.2p1
- add more examples to ntp.conf

* Thu Jul 06 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2-3
- fix manycast support in ntpdate (#194329)
- reply to manycast requests with null refid
- enable mlockall (#195617)
- correct threshold value in ntpdate manpage

* Wed Jun 14 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2-2
- update initscript, ntp.conf, man pages
- package sntp

* Mon Jun 12 2006 Miroslav Lichvar <mlichvar@redhat.com> 4.2.2-1
- update to ntp-4.2.2
- drop drift file upgrade script
- use proper CFLAGS for ntpstat

* Thu May 11 2006 Miroslav Lichvar <mlichvar@redhat.com> - 4.2.0.a.20050816-14
- modify ntp.conf, change default restrict, remove broadcastdelay,
  use fedora.pool.ntp.org (#189667)
- don't install drift file
- remove unsupported options from ntptrace manpage (#137717)
- fix default paths in manpages for ntp-keygen and ntpdate

* Fri Apr 07 2006 Miroslav Lichvar <mlichvar@redhat.com> - 4.2.0.a.20050816-13
- add option to sync hwclock after ntpdate (#179571)

* Fri Mar 31 2006 Miroslav Lichvar <mlichvar@redhat.com> - 4.2.0.a.20050816-12
- fix initscript:
  - replace -U with -u in getopts (#187003)
  - don't pass group to ntpdate -U argument and ignore -i in options (#142926)
  - set ntpconf for -c
  - remove -p 8 from ntpdate arguments
  - don't call ntpdate when step-tickers doesn't contain anything useful
    and -x isn't in options
- fix default keyfile for ntpdate (#183196)

* Thu Feb 23 2006 Miroslav Lichvar <mlichvar@redhat.com> - 4.2.0.a.20050816-11
- update man pages (#153195, #162856)
- drop C-Frame-121, vsnprintf, minusTi and loconly patch
- prevent segfault when loopback interface is not configured (#159056)
- spec cleanup

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.2.0.a.20050816-10.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.2.0.a.20050816-10.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 9 2005 Petr Raszyk <praszyk@redhat.com> 4.2.0.a.20050816-10
- ntpd does not submit his local clock (if there is no peer).
  ntpdate->ntpd #163862 , Patch13: ntp-stable-4.2.0a-20050816-loconly.patch

* Wed Nov 2 2005 Petr Raszyk <praszyk@redhat.com> 4.2.0.a.20050816-9
- Wrong parameter -T   -i
- Patch ntp-stable-4.2.0a-20050816-minusTi.patch

* Mon Oct 31 2005 Petr Raszyk <praszyk@redhat.com> 4.2.0.a.20050816-3
- A similar patch as ntp-4.0.99j-vsnprintf.patch in FEDORA CORE 4
- (current patch is ntp-stable-4.2.0a-20050816-vsnprintf.patch)

* Tue Sep 27 2005 Petr Raszyk <praszyk@redhat.com> 4.2.0.a.20050816-2
- Fix fails on upgrade, if ntpd is disabled (#166773)
- A cosmetic patch. There are some comments and braces '{' '}' added.
- One unprintable character was converted to octal-form .
- It can be removed anytime (conversion of the cvs-projets for C-Frame 121,
- (auto-debug, auto-trace for cfr-printnet server).

* Thu Aug 25 2005 Jindrich Novy <jnovy@redhat.com> 4.2.0.a.20050816-1
- update to the latest stable 4.2.0.a.20050816
- drop upstreamed .gcc4, .vsnprintf patches
- remove obsolete .autofoo patch
- make patch numbering less chaotic
- don't package backup for .droproot patch

* Thu Apr 14 2005 Jiri Ryska <jryska@redhat.com> 4.2.0.a.20040617-8
- fixed gid setting when ntpd started with -u flag (#147743)

* Tue Mar 08 2005 Jiri Ryska <jryska@redhat.com> 4.2.0.a.20040617-7
- removed -Werror
- patched for gcc4 and rebuilt

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> - 4.2.0.a.20040617-6
- Rebuilt for new readline.

* Mon Dec 13 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040617-5
- patched ntp to build with -D_FORTIFYSOURCE=2 -Wall -Wextra -Werror

* Mon Oct 11 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040617-4
- removed firewall hole punching from the initscript; rely on iptables
  ESTABLISHED,RELATED or manual firewall configuration

* Fri Oct  8 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040617-3
- improved postsection
- BuildRequires readline-devel
- PreReq grep

* Thu Sep 30 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040617-2
- set pool.ntp.org as the default timeserver pool

* Mon Sep 13 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040617-1
- version ntp-stable-4.2.0a-20040617

* Tue Aug 17 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040616-4
- added ntp-4.2.0-sbinpath.patch (bug 130536)

* Tue Aug 17 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040616-3
- added ntp-stable-4.2.0a-20040616-groups.patch (bug 130112)

* Thu Jul 29 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040616-2
- take chroot in account (bug 127252)

* Fri Jul 23 2004 Harald Hoyer <harald@redhat.com> - 4.2.0.a.20040616-1
- new version ntp-stable-4.2.0a-20040616
- removed most patches

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Mar 11 2004 Harald Hoyer <harald@redhat.com> - 4.2.0-7
- ntpgenkey fixed (117378)
- fixed initscript to call ntpdate with -U (117894)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Harald Hoyer <harald@faro.stuttgart.redhat.com> - 4.2.0-5
- readded ntp-wait and ntptrace
- new filter-requires to prevent perl dependency

* Mon Jan 26 2004 Harald Hoyer <harald@redhat.de> 4.2.0-4
- added autofoo patch

* Tue Oct 28 2003 Harald Hoyer <harald@redhat.de> 4.2.0-3
- removed libmd5 dependency
- removed perl dependency

* Tue Oct 28 2003 Harald Hoyer <harald@redhat.de> 4.2.0-2
- fixed initscript to use new FW chain name

* Mon Oct 27 2003 Harald Hoyer <harald@redhat.de> 4.2.0-1
- 4.2.0
- added PIE

* Thu Sep 11 2003 Harald Hoyer <harald@redhat.de> 4.1.2-4
- changed ntp.conf driftfile path #104207

* Fri Aug 29 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- also build as non-root

* Thu Aug 28 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-2
- added ntpstat
- added manpages

* Tue Jul 01 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-1.rc3.5
- move driftfile to /var

* Tue Jul 01 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-1.rc3.4
- make a seperate directory for drift
- security fix, patch ntp-4.1.1c-rc3-authkey.patch #96927
 
* Wed Jun 18 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-1.rc3.3
- %%{_sysconfdir}/ntp/drift.TEMP needs to be writable by ntp #97754
- no duplicate fw entries #97624

* Wed Jun 18 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-1.rc3.2
- changed permissions of config files  

* Tue Jun 17 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-1.rc3.1
- updated to rc3 

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-0.rc2.2
- corrected pid file name in %%{_sysconfdir}/sysconfig/ntpd

* Mon Apr 28 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-0.rc2.1
- update to 4.1.1rc2

* Tue Feb 25 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-0.rc1.3
- better awk for timeservers #85090, #82713, #82714

* Thu Feb 13 2003 Harald Hoyer <harald@redhat.de> 0:4.1.2-0.rc1.2
- added loopfilter patch, -x should work now!
- removed slew warning

* Mon Feb 10 2003 Harald Hoyer <harald@redhat.de> 1:4.1.1-2
- ok, messed up with the versions... added epoch :(

* Fri Feb 07 2003 Harald Hoyer <harald@redhat.de> 4.1.1-1
- going back to stable 4.1.1 with the limit patch
- added limit patch
- added slew warning

* Thu Jan 30 2003 Harald Hoyer <harald@redhat.de> 4.1.73-2
- removed exit on ntpdate fail, better add '-g' option

* Wed Jan 29 2003 Harald Hoyer <harald@redhat.de> 4.1.73-1
- update to version 4.1.73
- removed most of the patches
- limit ntp_adjtime parameters

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Harald Hoyer <harald@redhat.de> 4.1.1b-1
- updated to version 4.1.1b
- improved initscript - use ntpdate on -x
- improved initscript - open firewall only for timeservers
- ntp-4.1.1a-adjtime.patch removed (already in source)
- ntp-4.1.1a-mfp.patch removed (already in source)
- ntp-4.0.99j-vsnprintf.patch removed (already in source)

* Tue Nov 19 2002 Harald Hoyer <harald@redhat.de> 4.1.1a-12
- added adjtime patch #75558

* Wed Nov 13 2002 Harald Hoyer <harald@redhat.de>
- more ntpd.init service description #77715

* Mon Nov 11 2002 Harald Hoyer <harald@redhat.de>
- ntp-4.1.1a-mfp.patch fixes #77086

* Sat Aug 31 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add option -n to initscript to avoid DNS lookups #72756

* Fri Aug 23 2002 Jeremy Katz <katzj@redhat.com>
- service should fail to start ntpd if running ntpdate fails

* Tue Aug 20 2002 Harald Hoyer <harald@redhat.de>
- added two more 'echo's in the initscript

* Thu Aug 15 2002 Harald Hoyer <harald@redhat.de>
- added firewall opener in initscript

* Tue Jul 23 2002 Harald Hoyer <harald@redhat.de>
- removed libelf dependency
- removed stripping

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Harald Hoyer <harald@redhat.de> 4.1.1a-3
- refixed #46464
- another genkeys/snprintf bugfix

* Wed May 22 2002 Harald Hoyer <harald@redhat.de> 4.1.1a-1
- update to version 4.1.1a

* Mon Apr 08 2002 Harald Hoyer <harald@redhat.de> 4.1.1-1
- update to 4.1.1 (changes are minimal)
- more examples in default configuration

* Tue Apr 02 2002 Harald Hoyer <harald@redhat.de> 4.1.0b-6
- more secure default configuration (#62238)

* Mon Jan 28 2002 Harald Hoyer <harald@redhat.de> 4.1.0b-5
- more regex magic for the grep (#57837)

* Mon Jan 28 2002 Harald Hoyer <harald@redhat.de> 4.1.0b-4
- created drift with dummy value #58294
- grep for timeservers in ntp.conf also for ntpdate #57837
- check return value of ntpdate #58836

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 4.1.0b-3
- automated rebuild

* Tue Jan 08 2002 Harald Hoyer <harald@redhat.de> 4.1.0b-2
- added --enable-all-clocks --enable-parse-clocks (#57761)

* Thu Dec 13 2001 Harald Hoyer <harald@redhat.de> 4.1.0b-1
- bumped version
- fixed #57391, #44580
- set startup position to 58 after named

* Wed Sep 05 2001 Harald Hoyer <harald@redhat.de> 4.1.0-4
- fixed #53184

* Tue Sep 04 2001 Harald Hoyer <harald@redhat.de> 4.1.0-3
- fixed #53089 /bin/nologin -> /sbin/nologin

* Fri Aug 31 2001 Harald Hoyer <harald@redhat.de> 4.1.0-2
- fixed #50247 thx to <enrico.scholz@informatik.tu-chemnitz.de>

* Thu Aug 30 2001 Harald Hoyer <harald@redhat.de> 4.1.0-1
- wow, how stupid can a man be ;).. fixed #50698 
- updated to 4.1.0 (changes are small and in non-critical regions)

* Wed Aug 29 2001 Harald Hoyer <harald@redhat.de> 4.0.99mrc2-5
- really, really :) fixed #52763, #50698 and #50526

* Mon Aug 27 2001 Tim Powers <timp@redhat.com> 4.0.99mrc2-4
- rebuilt against newer libcap
- Copyright -> license

* Wed Jul 25 2001 Harald Hoyer <harald@redhat.com> 4.0.99mrc2-3
- integrated droproot patch (#35653)
- removed librt and libreadline dependency 

* Sat Jul  7 2001 Tim Powers <timp@redhat.com>
- don't build build sgid root dirs

* Mon Jun 18 2001 Harald Hoyer <harald@redhat.de>
- new snapshot
- removed typos and security patch (already there)
- commented multicastclient in config file

* Thu Jun 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- call libtoolize to compile on newer archs

* Mon Apr  9 2001 Preston Brown <pbrown@redhat.com>
- remove ghost files make RHN happy
- modify initscript to match accordingly

* Fri Apr  6 2001 Pekka Savola <pekkas@netcore.fi>
- Add the remote root exploit patch (based on ntp-hackers).
- Enhance droproot patch (more documentation, etc.) <Jarno.Huuskonen@uku.fi>
- Tweak the droproot patch to include sys/prctl.h, not linux/prctl.h
(implicit declarations)
- Remote groupdel commands, shouldn't be needed.
- Removed -Wcast-qual and -Wconversion due to excessive warnings (hackish).
- Make ntp compilable with both glibc 2.1 and 2.2.x (very dirty hack)
- Add %%{_sysconfdir}/sysconfig/ntpd which drops root privs by default

* Thu Apr  5 2001 Preston Brown <pbrown@redhat.com>
- security patch for ntpd

* Mon Mar 26 2001 Preston Brown <pbrown@redhat.com>
- don't run configure macro twice (#32804)

* Sun Mar 25 2001 Pekka Savola <pekkas@netcore.fi>
- require/buildprereq libcap/libcap-devel
- use 'ntp' user, tune the pre/post scripts, %%files
- add $OPTIONS to the init script

* Tue Mar 20 2001 Jarno Huuskonen <Jarno.Huuskonen@uku.fi>
- droproot/caps patch
- add ntpd user in pre
- make %%{_sysconfdir}/ntp ntpd writable

* Mon Mar  5 2001 Preston Brown <pbrown@redhat.com>
- allow comments in %%{_sysconfdir}/ntp/step-tickers file (#28786).
- need patch0 (glibc patch) on ia64 too

* Tue Feb 13 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- also set prog=ntpd in initscript

* Tue Feb 13 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- use "$prog" instead of "$0" for the init script

* Thu Feb  8 2001 Preston Brown <pbrown@redhat.com>
- i18n-neutral .init script (#26525)

* Tue Feb  6 2001 Preston Brown <pbrown@redhat.com>
- use gethostbyname on addresses in %%{_sysconfdir}/ntp.conf for ntptime command (#26250)

* Mon Feb  5 2001 Preston Brown <pbrown@redhat.com>
- start earlier and stop later (#23530)

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script (#26078)

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- typo in ntp.conf (#23173).

* Mon Dec 11 2000 Karsten Hopp <karsten@redhat.de>
- rebuilt to fix permissions of /usr/share/doc/ntp-xxx

* Thu Nov  2 2000 Jeff Johnson <jbj@redhat.com>
- correct mis-spellings in ntpq.htm (#20007).

* Thu Oct 19 2000 Jeff Johnson <jbj@redhat.com>
- add %%ghost %%{_sysconfdir}/ntp/drift (#15222).

* Wed Oct 18 2000 Jeff Johnson <jbj@redhat.com>
- comment out default values for keys, warn about starting with -A (#19316).
- take out -A from ntpd startup as well.
- update to 4.0.99k.

* Wed Aug 23 2000 Jeff Johnson <jbj@redhat.com>
- use vsnprintf rather than vsprintf (#16676).

* Mon Aug 14 2000 Jeff Johnson <jbj@redhat.com>
- remove Conflicts: so that the installer is happy.

* Tue Jul 25 2000 Jeff Johnson <jbj@redhat.com>
- workaround glibc-2.1.90 lossage for now.

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 26 2000 Preston Brown <pbrown@redhat.com>
- move and update init script, update post/preun/postun scripts

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- noreplace ntp.conf,keys files

* Mon Jun 12 2000 Jeff Johnson <jbj@redhat.com>
- Create 4.0.99j package.
- FHS packaging.
