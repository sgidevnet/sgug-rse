Name:           rf
Version:        0.4.18
Release:        13%{?dist}
Summary:        Read feeds from any source

License:        GPLv3+
URL:            http://code.google.com/p/readfeed
Source0:        http://readfeed.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildArch:      noarch

Requires:       sed
Requires:       bash
Requires:       gawk
Requires:       curl
Requires:       coreutils
Requires:       util-linux
Requires:       lynx
Requires:       xmlstarlet

%description
Read feed is a command that reads feeds from any source. read feed uses
the feed of a site to manage it with a command line interface.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
export AM_UPDATE_INFO_DIR=no
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.18-4
- Follow unversioned doc policy.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.18-2
- Fix bug number in spec.

* Wed May 08 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.18-1
- Update to mainstream.

* Wed May 1 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.16-1
- Update to mainstream.

* Mon Apr 29 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.14-1
- Update to mainstream.

* Sun Apr 28 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.12-2
- Fedora review request (bug 957520).

* Sun Apr 28 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.12-1
- Update to mainstream.

* Fri Apr 12 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.8-1
- Update to mainstream.

* Fri Mar 15 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.6-1
- Version update.

* Wed Jan 02 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.2-1
- Improve doc install.
- Fix changelog macros.
- Use more generic man and info %%files.
- Remove obsolete "rm -rf $RPM_BUILD_ROOT".
- Use GPLv3+.
- Omit deprecated stuff like BuildRoot, Group, clean and defattr.
- Omit Requires: glibc-common, implicitly pulled by pretty much everything already.
- Conform to rpmlint.
- Reformat description from too long single line.
- BuildRequires and Requires entries listed one-by-one for a better spec legibility.
- Fix Source* tag to the full URL for the compressed archive containing the (original) pristine source code.
- Fix license to GPLv3.
- Add Changelog.
- Fedora review request (bug pending).

