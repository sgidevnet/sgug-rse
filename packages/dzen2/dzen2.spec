Name:           dzen2
Version:        0.8.5
Release:        24.20100104svn%{?dist}
Summary:        A general purpose messaging and notification program

License:        MIT
URL:            https://github.com/robm/dzen
# created with dzen2-tarballl 20100-01-04
Source0:        %{name}-%{version}-2010-01-04.tar.gz
#Source0:        http://gotmor.googlepages.com/%{name}-latest.tar.gz
Source1:        dzen2.1
Source2:        dzen2-dbar.1
Source3:        dzen2-gcpubar.1
Source4:        dzen2-gdbar.1
Source5:        dzen2-textwidth.1
# tarball generation script
Source10:       dzen2-tarball

# 2007-12-26: sent to upstream via private e-mail, inclusion depends on usability
# for *BSD and Solaris
#Patch0:         dzen2-0.8.5-check_environment.patch
# Not sent to upstream: removes strip and shows cc invocations, which seems not to
#                       be wanted by upstream
Patch1:         dzen2-0.8.5-2010-01-04-verbose.patch
Patch2:         dzen2-0.8.5-2010-01-04-fedora-config.patch

BuildRequires:  gcc
BuildRequires:  libXpm-devel libXinerama-devel
# for /usr/include/X11/Xft/Xft.h
BuildRequires:  libXft-devel

%description
Dzen is a general purpose messaging, notification and menuing program for X11.
It was designed to be scriptable in any language and integrate well with window
managers like dwm, wmii and xmonad, though it will work with any windowmanger.


%prep
%setup -q -n %{name}-%{version}-2010-01-04
#%patch0 -p1 -b .check_environment
%patch1 -p1 -b .verbose
%patch2 -p1 -b .fedora-config


%build
make %{?_smp_mflags} LIBDIR="%{_libdir}"
make -C gadgets %{?_smp_mflags} LIBDIR="%{_libdir}"


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
export CFLAGS="${RPM_OPT_FLAGS}"
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}
make -C gadgets install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}
for gadget in dbar gcpubar gdbar textwidth
do
mv $RPM_BUILD_ROOT%{_bindir}/{,dzen2-}"${gadget}"
done

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
for manpage in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}
do
install -m 0644 "${manpage}" $RPM_BUILD_ROOT%{_mandir}/man1/"${manpage##*/}"
done



%files
# There is no .desktop file, because the applications displays data received
# via stdin, e.g. from xmonad, a window manager
# This cannot be done using a .desktop file
%doc LICENSE CREDITS README README.dzen
%doc gadgets/README.*
%{_bindir}/dzen2
%{_bindir}/dzen2-dbar
%{_bindir}/dzen2-gcpubar
%{_bindir}/dzen2-gdbar
%{_bindir}/dzen2-textwidth
%{_mandir}/man1/dzen2.1*
%{_mandir}/man1/dzen2-dbar.1*
%{_mandir}/man1/dzen2-gcpubar.1*
%{_mandir}/man1/dzen2-gdbar.1*
%{_mandir}/man1/dzen2-textwidth.1*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-24.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-23.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-22.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-21.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-20.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-19.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-18.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-17.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-16.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-15.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-14.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-13.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-12.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-11.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-10.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 28 2011 Till Maas <opensource@till.name> - 0.8.5-9.20100104svn
- Re-add incorrectly removed %%build section (Red Hat Bug 680994)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-8.20100104svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 04 2010 Till Maas <opensource@till.name> - 0.8.5-7.20100104svn
- Update to svn snapshot to support Xft and docking RedHat Bugzilla #552386

* Wed Sep 16 2009 Till Maas <opensource@till.name> - 0.8.5-6
- Fix some typos in %%description

* Thu Aug 27 2009 Till Maas <opensource@till.name> - 0.8.5-5
- Remove uneeded PREFIX= argument to make in %%build

* Wed Aug 26 2009 Till Maas <opensource@till.name> - 0.8.5-4
- export LDFLAGS
- explain missing .desktop file

* Tue Aug 25 2009 Till Maas <opensource@till.name> - 0.8.5-3
- use make -C instead of pushd/popd
- add manpages from debian
- prefix gadgets with dzen2 like debian does it

* Tue Mar 31 2009 Till Maas <opensource@till.name> - 0.8.5-2
- Add description

* Sat Nov 01 2008 Till Maas <opensource@till.name> - 0.8.5-1
- Initial package for Fedora
