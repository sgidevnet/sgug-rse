# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: Powerful interactive shell
Name: zsh
Version: 5.8
Release: 2%{?dist}
License: MIT
URL: http://zsh.sourceforge.net/
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: zlogin.rhs
Source2: zlogout.rhs
Source3: zprofile.rhs
Source4: zshrc.rhs
Source5: zshenv.rhs
Source6: dotzshrc

BuildRequires: autoconf
BuildRequires: coreutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: gdbm-devel
#BuildRequires: glibc-langpack-ja
#BuildRequires: libcap-devel
BuildRequires: ncurses-devel
BuildRequires: pcre-devel
BuildRequires: sed
#BuildRequires: texi2html
BuildRequires: texinfo
Requires(post): grep
Requires(postun): coreutils grep

# the hostname package is not available on RHEL-6
%if 12 < 0%{?fedora} || 6 < 0%{?rhel}
BuildRequires: hostname
%else
# /bin and /usr/bin are separate directories on RHEL-6
#%%define _bindir /bin
%endif

Provides: %{_prefix}/bin/zsh
#AutoReq: no

%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

%package html
Summary: Zsh shell manual in html format
BuildArch:	noarch

%description html
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in html format.

%prep
%autosetup -p1
autoreconf -fiv

#Rewrite shebangs
perl -pi -e "s|/usr/local/bin/zsh|%{_prefix}/bin/zsh|g" Misc/globtests
perl -pi -e "s|/usr/local/bin/zsh|%{_prefix}/bin/zsh|g" Misc/globtests.ksh
perl -pi -e "s|/usr/local/bin/zsh|%{_prefix}/bin/zsh|g" Util/reporter

perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Test/runtests.zsh
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Test/ztst.zsh
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Util/check-tmux-state
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/zed
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/checkmail
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/run-help
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/zkbd
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/run-help-ip
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/zcalc
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Misc/sticky-note
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Calendar/calendar_add
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Example/cat
perl -pi -e "s|/bin/zsh|%{_prefix}/bin/zsh|g" Functions/Example/zless

# enable parallel build
sed -e 's|^\.NOTPARALLEL|#.NOTPARALLEL|' -i 'Config/defs.mk.in'

%build

# make build of run-time loadable modules work again (#1535422)
%undefine _strict_symbol_defs_build

# make loading of module's dependencies work again (#1277996)
export LIBLDFLAGS='-z lazy'

# avoid build failure in case we have working ypcat (#1687574)
export zsh_cv_sys_nis='no'

export LDFLAGS="-Wl,-rpath -Wl,%{_libdir}/zsh $RPM_LD_FLAGS"

# Not activated for irix
#    --enable-maildir-support \ #

%configure \
    --enable-etcdir=%{_sysconfdir} \
    --with-tcsetpgrp \
    --enable-pcre

# prevent the build from failing while running in parallel
make -C Src headers
make -C Src -f Makemod zsh{path,xmod}s.h version.h

make %{?_smp_mflags} all html

%check
# Run the testsuite
make check

%install
%make_install install.info \
  fndir=%{_datadir}/%{name}/%{version}/functions \
  sitefndir=%{_datadir}/%{name}/site-functions \
  scriptdir=%{_datadir}/%{name}/%{version}/scripts \
  sitescriptdir=%{_datadir}/%{name}/scripts \
  runhelpdir=%{_datadir}/%{name}/%{version}/help

rm -f $RPM_BUILD_ROOT%{_bindir}/zsh-%{version}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    install -m 644 $i $RPM_BUILD_ROOT%{_sysconfdir}/"$(basename $i .rhs)"
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zshrc


%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
#    echo "/bin/%{name}" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
#    grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
#  sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi


%files
%doc README LICENCE Etc/BUGS Etc/CONTRIBUTORS Etc/FAQ FEATURES MACHINES
%doc NEWS Etc/zsh-development-guide Etc/completion-style-guide
%attr(755,root,root) %{_bindir}/zsh
%{_mandir}/*/*
%{_infodir}/*
%{_datadir}/zsh
%{_libdir}/zsh
%config(noreplace) %{_sysconfdir}/skel/.z*
%config(noreplace) %{_sysconfdir}/z*

%files html
%doc Doc/*.html

%changelog
* Mon Feb 24 2020 Kamil Dudka <kdudka@redhat.com> - 5.8-1
- update to latest upstream release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Kamil Dudka <kdudka@redhat.com> - 5.7.1-4
- make failed searches of history in Zle robust (#1722703)

* Tue Mar 12 2019 Kamil Dudka <kdudka@redhat.com> - 5.7.1-3
- avoid build failure in case we have working ypcat (#1687574)

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 5.7.1-2
- Remove obsolete requirements for %%post/%%preun scriptlets

* Mon Feb 04 2019 Kamil Dudka <kdudka@redhat.com> - 5.7.1-1
- update to latest upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 5.7-1
- Update to latest upstream release.

* Fri Nov 30 2018 Kamil Dudka <kdudka@redhat.com> - 5.6.2-3
- return non-zero exit status on nested parse error (#1654989)

* Mon Nov 12 2018 Kamil Dudka <kdudka@redhat.com> - 5.6.2-2
- fix programming mistakes detected by static analysis

* Fri Sep 14 2018 Kamil Dudka <kdudka@redhat.com> - 5.6.2-1
- update to latest upstream release

* Mon Sep 10 2018 Kamil Dudka <kdudka@redhat.com> - 5.6.1-1
- update to latest upstream release

* Tue Sep 04 2018 Kamil Dudka <kdudka@redhat.com> - 5.6-1
- update to latest upstream release (fixes CVE-2018-0502 and CVE-2018-13259)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Kamil Dudka <kdudka@redhat.com> - 5.5.1-1
- update to latest upstream release

* Mon Apr 09 2018 Kamil Dudka <kdudka@redhat.com> - 5.5-1
- update to latest upstream release, which fixes the following vulnerabilities:
    CVE-2018-1100 - stack-based buffer overflow in utils.c:checkmailpath()
    CVE-2018-1083 - stack-based buffer overflow in compctl.c:gen_matches_files()
    CVE-2018-1071 - stack-based buffer overflow in exec.c:hashcmd()

* Tue Mar 06 2018 Kamil Dudka <kdudka@redhat.com> - 5.4.2-7
- avoid crash when copying empty hash table (CVE-2018-7549)
- avoid NULL dereference when using ${(PA)...} on an empty array (CVE-2018-7548)

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> - 5.4.2-6
- add explicit BR for the gcc compiler

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Kamil Dudka <kdudka@redhat.com> - 5.4.2-4
- make build of run-time loadable modules work again (#1535422)

* Tue Jan 16 2018 Kamil Dudka <kdudka@redhat.com> - 5.4.2-3
- rebuild against latest gdbm-devel (#1533176)

* Wed Oct 04 2017 Kamil Dudka <kdudka@redhat.com> - 5.4.2-2
- make the call depth limit configurable by $FUNCNEST (#1441092)

* Mon Aug 28 2017 Kamil Dudka <kdudka@redhat.com> - 5.4.2-1
- update to latest upstream release

* Wed Aug 09 2017 Kamil Dudka <kdudka@redhat.com> - 5.4.1-1
- update to latest upstream release

* Tue Aug 01 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-12
- use %%make_install instead of %%makeinstall, which is deprecated
- modernize spec file (Group tag, %%clean, %%defattr)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-10
- enable parallel build

* Wed Jun 14 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-9
- fix unsafe use of a static buffer in history isearch (#1461483)

* Thu Jun 08 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-8
- make the zsh-html subpackage noarch (#1459657)

* Thu May 25 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-7
- drop unmaintained and undocumented zshprompt.pl script

* Wed May 17 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-6
- drop workaround for broken terminals over serial port (#56353)

* Thu May 11 2017 Kamil Dudka <kdudka@redhat.com> - 5.3.1-5
- compile with -fconserve-stack to prevent stack overflow (#1441092)

* Fri Mar 31 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 5.3.1-4
- Add build deps on gdbm-devel and pcre-devel.  Pass --enable-pcre to
  configure.  These should ensure that the pcre and gdbm modules are built.
  (#1438009)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Kamil Dudka <kdudka@redhat.com> - 5.3.1-2
- do not require the hostname package when being built on RHEL-6

* Wed Dec 21 2016 Kamil Dudka <kdudka@redhat.com> - 5.3.1-1
- Update to latest upstream release: Zsh 5.3.1

* Wed Dec 14 2016 Kamil Dudka <kdudka@redhat.com> - 5.3-2
- drop zsh-4.3.6-8bit-prompts.patch which was superseeded by an upstream patch
  (see http://www.zsh.org/mla/users/2007/msg00468.html for details)
- drop undocumented zsh-test-C02-dev_fd-mock.patch

* Tue Dec 13 2016 Kamil Dudka <kdudka@redhat.com> - 5.3-1
- apply patches automatically to ease maintenance
- Update to latest upstream release: Zsh 5.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Kamil Dudka <kdudka@redhat.com> - 5.2-4
- prevent zsh from crashing when printing the "out of memory" message (#1300958)

* Thu Jan 07 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 5.2-3
- Add patch to fix VCS_INFO_nbvsformats bug.

* Fri Dec 25 2015 Adrien Vergé <adrienverge@gmail.com> - 5.2-2
- update zsh completion script for dnf to the latest upstream version

* Thu Dec 03 2015 Kamil Dudka <kdudka@redhat.com> - 5.2-1
- Update to latest upstream release: Zsh 5.2

* Thu Nov 05 2015 Kamil Dudka <kdudka@redhat.com> - 5.1.1-3
- make loading of module's dependencies work again (#1277996)

* Thu Oct 08 2015 Kamil Dudka <kdudka@redhat.com> - 5.1.1-2
- fix crash in ksh mode with -n and $HOME (#1269883)

* Mon Sep 14 2015 Kamil Dudka <kdudka@redhat.com> - 5.1.1-1
- Update to latest upstream release: Zsh 5.1.1

* Mon Aug 31 2015 Kamil Dudka <kdudka@redhat.com> - 5.1-1
- Update to latest upstream release: Zsh 5.1
- remove outdated workarounds in %%check

* Thu Jul 30 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.8-6
- fix handling of command substitution in math context

* Wed Jul 22 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.8-5
- prevent infinite recursion in ihungetc() (#1245712)

* Tue Jul 07 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.8-4
- backport completion for dnf (#1239337)

* Thu Jul 02 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.8-3
- backport completion-related upstream fixes (#1238544)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.8-1
- Update to latest upstream release: Zsh 5.0.8

* Fri May 22 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.7-8
- fix SIGSEGV of the syntax check in ksh emulation mode (#1222867)

* Mon Apr 20 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.7-7
- fix SIGSEGV when handling heredocs and keyboard interrupt (#972624)
- queue signals when manipulating global state to avoid deadlock

* Sun Jan 25 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.7-6
- use correct allocation function in the new 'cd' code (#1183238)

* Fri Jan 23 2015 Kamil Dudka <kdudka@redhat.com> - 5.0.7-5
- suppress a warning about closing an already closed file descriptor (#1184002)
- improve handling of NULL in the 'cd' built-in (#1183238)

* Wed Nov 19 2014 Kamil Dudka <kdudka@redhat.com> - 5.0.7-4
- update documentation of POSIX_JOBS in the zshoptions.1 man page (#1162198)

* Tue Nov 18 2014 Kamil Dudka <kdudka@redhat.com> - 5.0.7-3
- replace an incorrect comment in /etc/zshenv (#1164313)

* Mon Nov 10 2014 Kamil Dudka <kdudka@redhat.com> - 5.0.7-2
- make the wait built-in work for already exited processes (#1162198)

* Wed Oct 08 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.7-1
- Update to latest upstream release: Zsh 5.0.7

* Thu Aug 28 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.6-1
- Update to latest upstream release: Zsh 5.0.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.5-7
- apply upstream patch which fixes CPU load issue (RHBZ#1120424)

* Wed Jul 09 2014 Adam Jackson <ajax@redhat.com> 5.0.5-6
- Fix missing 'fi' in %%post

* Thu Jul 03 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.5-5
- improve handling of /etc/shells

* Wed Jul 02 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.5-4
- fix FTBFS issue (RHBZ#1106713)
- remove individual _bindir setting; install to /usr/bin/ (RHBZ#1034060)
- require info package instead of /sbin/install-info binary

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.5-1
- Update to latest upstream release: Zsh 5.0.5

* Thu Jan 16 2014 James Antill <james@fedoraproject.org> - 5.0.2-8
- Remove unneeded build require on tetex.

* Sat Oct 26 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.2-7
- Require hostname package instead of /bin/hostname

* Tue Oct 22 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.2-6
- remove systemd completion, it delivers it's own now (RHBZ#1022039)

* Thu Aug 01 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.2-5
- update systemd completion (adds machinectl command)

* Tue Jun 25 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.2-4
- up-to-date systemd completion (#949003)
- apply patch for building for aarch64 (#926864)

* Mon Apr 15 2013 James Antill <james@fedoraproject.org> - 5.0.2-3
- Fix the changelog dates.
- Fix the texi itemx bug.
- Resolves: bug#927863

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.2-1
- Update to new upstream version: Zsh 5.0.2

* Wed Nov 21 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 5.0.0-1
- Update to new upstream version: Zsh 5.0.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.17-1
- Update to new upstream version: Zsh 4.3.17

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.15-1
- Update to new upstream version: Zsh 4.3.15

* Sat Dec 17 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.14-2
- change the License field to MIT (RHBZ#768548)

* Sat Dec 10 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.14-1
- Update to new upstream version: Zsh 4.3.14

* Sat Dec 03 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.13-1
- Update to new upstream version: Zsh 4.3.13

* Sat Aug 13 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 4.3.12-1
- Update to new upstream version: Zsh 4.3.12

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Christopher Ailon <caillon@redhat.com> - 4.3.11-1
- Rebase to upstream version 4.3.11

* Tue Dec 7 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 4.3.10-6
- Rebuild for FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=631197
- Remove deprecated PreReq, the packages aren't needed at runtime and they're
  already in Requires(post,preun,etc): lines.

* Mon Mar 22 2010 James Antill <james@fedoraproject.org> - 4.3.10-5
- Add pathmunge to our /etc/zshrc, for profile.d compat.
- Resolves: bug#548960

* Fri Aug  7 2009 James Antill <james@fedoraproject.org> - 4.3.10-4
- Allow --excludedocs command to work!
- Resolves: bug#515986

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 James Antill <james@fedoraproject.org> - 4.3.10-1
- Import new upstream 4.3.10

* Wed Jun 10 2009 Karsten Hopp <karsten@redhat.com> 4.3.9-4.1
- skip D02glob test on s390, too

* Mon Mar  2 2009 James Antill <james@fedoraproject.org> - 4.3.9-4
- Remove D02glob testcase on ppc/ppc64, and hope noone cares

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
