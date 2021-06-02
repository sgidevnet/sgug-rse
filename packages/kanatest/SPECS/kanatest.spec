%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev  19dd1a7df9e1cd1c72a47b091ffeac5c0eabb354
%global git_date 20170810
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version D%{git_date}git%{git_short}
%endif

%global mainver 0.4.10
%global mainrel 0.1

Name:           kanatest
Version:        %{mainver}
Release:        %{mainrel}%{?git_version:.%{?git_version}}%{?dist}.4
Summary:        Hiragana and Katakana drill tool

License:        GPLv2+
URL:            http://clayo.org/kanatest/
%if 0%{?git_snapshot}
Source0:        %{name}-%{version}-%{?git_version}.tar.bz2
%else
Source0:        http://clayo.org/kanatest/%{name}-%{version}.tar.gz
%endif
# Shell script to create tarball from git scm
Source100:      create-tarball-from-git.sh

BuildRequires:  desktop-file-utils >= 0.9
BuildRequires:  gtk2-devel >= 2.0
BuildRequires:  libxml2-devel
BuildRequires:  gettext
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires:       font(:lang=ja)
Requires:       hicolor-icon-theme

%description
Kanatest is a simple, GTK 2-based kana drill tool. It offers three drill modes:
hiragana, katakana, and mixed mode. The tester shows random kana characters
and waits until you enter the romaji equivalent in an entry field. At the end,
statistics are provided

%prep
%setup -q %{?git_version:-n %{name}-%{version}-%{?git_version}}

sed -i \
	src/Makefile.in \
%if 0%{?git_snapshot}
	src/Makefile.am \
%endif
	-e 's|DISABLE_DEPRECATED|ENABLE_DEPRECATED|g'

%build
%if 0%{?git_snapshot}
bash autogen.sh
%endif

export PLATFORM_CFLAGS="$RPM_OPT_FLAGS -Werror-implicit-function-declaration"
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}



%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/kanatest
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/kanatest.png
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-0.1.D20170810git19dd1a7d.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-0.1.D20170810git19dd1a7d.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-0.1.D20170810git19dd1a7d.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-0.1.D20170810git19dd1a7d.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.10-0.1.D20170810git19dd1a7d
- Update to the latest git (bug 1510114)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.8-18
- Modify gtk_message_dialog_new_with_markup() usage
  for result dialog
- Fix bug 1308898

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.8-16
- Disable GDK_PIXBUF_DISABLE_DEPRECATED and so on (to use
  deprecated functions)
- Add -Werror-implicit-function-declaration to check this
- Fix bug 1296655

* Sun Jul 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.8-15
- format security build fix

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.8-7
- Rebuild for new libpng

* Tue Aug 02 2011 Robert Marcano <robert@marcanoonline.com> - 0.4.8-6
- Remove Japanese bitmap fonts dependency 

* Sat Jun 25 2011 Robert Marcano <robert@marcanoonline.com> - 0.4.8-5
- Fix Bug 631023 FTBFS
- Fix URL

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Robert Marcano <robert@marcanoonline.com> - 0.4.8-2
- Update to upstream release 0.4.8

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.4-6
- fix license tag

* Fri Apr 04 2008 Robert Marcano <robert@marcanoonline.com> - 0.4.4-5
- fix bug #249977: kanatest not built with $RPM_OPT_FLAGS

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.4-4
- Autorebuild for GCC 4.3

* Wed Sep 19 2007 Robert Marcano <robert@marcanoonline.com> - 0.4.4-3
- Update to upstream release 0.4.4

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.4.2-3
- Rebuild for selinux ppc32 issue.

* Thu Jun 21 2007 Robert Marcano <robert@marcanoonline.com> - 0.4.2-2
- Update to upstream release 0.4.2 - Bug 245177
- URL changed - Bug 245177

* Mon Aug 28 2006 Robert Marcano <robert@marcanoonline.com> - 0.3.6-6
- Rebuild

* Fri Jul 28 2006 Robert Marcano <robert@marcanoonline.com> - 0.3.6-5
- Fix build in mock (bug #200076)

* Mon Feb 13 2006 Robert Marcano <robert@marcanoonline.com> - 0.3.6-4
- Rebuild for Fedora Extras 5

* Fri May 20 2005 Robert Marcano <robert@marcanoonline.com> - 0.3.6-3
- Added desktop-file-utils to BuildRequires

* Mon May 09 2005 Robert Marcano <robert@marcanoonline.com> - 0.3.6-2
- Fix spec file following fedora-extras-list recomendations

* Sun May 08 2005 Robert Marcano <robert@marcanoonline.com> - 0.3.6-1
- Initial RPM release.
