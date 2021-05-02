Summary: The basic required files for the root user's directory
Name: rootfiles
Version: 8.1
Release: 25%{?dist}
License: Public Domain

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: dot-bashrc
Source1: dot-bash_profile
Source2: dot-bash_logout
Source3: dot-tcshrc
Source4: dot-cshrc

BuildArch: noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/root

for file in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
  f=`basename $file`
  install -p -m 644 $file $RPM_BUILD_ROOT/root/${f/dot-/.}
done

%posttrans
if [ $1 -eq 0 ] ; then
  #copy recursively the content, but do not overwrite the original files provided by rootfiles package
  cp -ndr --preserve=ownership,timestamps /etc/skel/. /root/ || :
fi

%files
%config(noreplace) /root/.[A-Za-z]*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Ondrej Vasik <ovasik@redhat.com> 0.1-16
- actually --no-preserve doesn't work for this case...
 - changing to --preserve

* Wed Dec 04 2013 Ondrej Vasik <ovasik@redhat.com> 0.1-15
- fix the posttrans scriptlet to not change the /root
  permissions (#1037688)

* Fri Sep 20 2013 Ondrej Vasik <ovasik@redhat.com> 0.1-14
- fix the posttrans copying (thanks O.Poplawski)

* Wed Sep 18 2013 Ondrej Vasik <ovasik@redhat.com> 0.1-13
- copy content of /etc/skel directory for root as posstrans,
  don't overwrite  existing files (#999114)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Ondrej Vasik <ovasik@redhat.com> - 8.1-5
- removed clear from dot-bash_logout (synchronized with bash,
  related to #429406)
- removed unset USERNAME from dot-bash_profile (synchronized with
  bash, related to #196735)

* Mon Mar 23 2009 Phil Knirsch <pknirsch@redhat.com> - 8.1-4
- Added the "we-are-upstream" comments according to Fedora review (#226376)
- Added -p option to install to preserve timestamps (#226376)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 31 2008 Ondrej Vasik <ovasik@redhat.com> - 8.1-2
- Add dist tag, fix a few rpmlint issues, rebuild due to
  wrong vendor (#451229)
- Added ncurses requirement(#469390)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 8.1-1.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  3 2004 Bill Nottingham <notting@redhat.com> 8.1-1
- restore tcsh prompt into .tcshrc (#141782)

* Wed Sep 22 2004 Bill Nottingham <notting@redhat.com> 8-1
- sync files with current /etc/skel stuff
- remove Xresources (#75666)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 7.2-5
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul  5 2001 Preston Brown <pbrown@redhat.com> 7.2-1
- /sbin stuff out of PATH, moved into /etc/profile

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 11 2000 Preston Brown <pbrown@redhat.com>
- fix .tcshrc

* Mon Jul  3 2000 Jakub Jelinek <jakub@redhat.com>
- don't assume ASCII ordering in glob pattern

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuild
- fix some path stuff (#11191)

* Tue Apr 18 2000 Bill Nottingham <notting@redhat.com>
- mv .Xdefaults -> .Xresources (#10623)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- add %%clean (#719)

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Wed Oct  9 1998 Bill Nottingham <notting@redhat.com>
- remove /root from %%files (it's in filesystem)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- portability fix for .cshrc (problem #235)
- change version to be same as release.

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Removed .Xclients and .Xsession from package, added %%pre to back up old
  .Xclients if necessary.
