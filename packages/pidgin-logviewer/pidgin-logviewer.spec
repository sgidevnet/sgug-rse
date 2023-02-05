%global snapshot_date 20110228
%global snapshot_revision 15
Name:           pidgin-logviewer
Version:        0.2 
Release:        25.%{snapshot_date}svn%{snapshot_revision}%{?dist}
Summary:        User-friendly and intuitive chat log viewer for Pidgin

License:        GPLv2
URL:            https://code.google.com/p/pidgin-logviewer/
#clone and tarred : svn export -r%%{snapshot_revision} http://pidgin-logviewer.googlecode.com/svn/trunk/ pidgin-logviewer-%%{version}
#tar -cvzf pidgin-logviewer-%%{version}svn%%{snapshot_revision}.tar.gz pidgin-logviewer-%%{version}
Source0:        %{name}-%{version}svn%{snapshot_revision}.tar.gz

BuildRequires:  pidgin-devel
BuildRequires:  automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
Requires:       pidgin

%description
This project aims to present an alternative, user-friendly and intuitive way 
of viewing chat logs in Pidgin. Currently the project is in an early stage,
and is designed as a plugin, but it eventually aims to replace Pidgin's default
log viewer.

%prep
%setup -q

echo "%{version}-%{release}" > version
autoreconf -fi

cd src
rm -rf .libs .deps *.o *.lo *.la



%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/pidgin/*.so


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-25.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-18.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-17.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-16.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-13.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11.20110228svn15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2-10.20110228svn15
- Rebuild for new libpng

* Mon Feb 28 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-9.20110228svn15
- Remove touch from build section

* Mon Feb 28 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-8.20110228svn15
- Fix version issue add patch to configure.ac

* Mon Feb 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-7.20110225svn14
- Fix autotools issue

* Mon Feb 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-6.20110216svn13
- Add global snapshot variables and fix tarball issue  

* Mon Feb 15 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-5.20110208svn13
- Fix svn export issue  

* Mon Feb 15 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-4.20110208svn13
- Add revision number in Release section and remove BUILDROOT section 

* Mon Feb 15 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-3.20110208svn13
- Removed all binary and add correction in Release section

* Fri Feb 11 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-2.20110208svn13
- Fix LICENSE contradiction

* Wed Feb 09 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.2-1.20110208svn13
- Initial RPM release
