Name:           ranger
Version:        1.9.2
Release:        4%{?dist}
Summary:        A vim-like file manager
License:        GPLv3+
URL:            https://ranger.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#Suggests:       w3m-img

%description
Ranger is a free console file manager that gives you greater flexibility and a
good overview of your files without having to leave your *nix console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right so you know where
you'll be going.


%prep
%autosetup
sed -i -e '1d;2i#!/usr/bin/python3' %{name}.py


%build
%py3_build


%install
%py3_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_pkgdocdir} _doc
find _doc -type f -exec chmod -R -x '{}' \;


%files
%license LICENSE
%doc _doc/*
%{_bindir}/ranger
%{_bindir}/rifle
%{python3_sitelib}/*
%{_datadir}/applications/ranger.desktop
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.2-2
- spec modernization thanks to Filip Szymański <fszymanski@fedoraproject.org>
- fixes rhbz #1592733 #1408563 #1495481 and #1559823

* Sun Oct 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.2-1
- update to latest version + spec cleanup, fixes rhbz #1408563

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 13 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.2-1
- update to 1.7.2

* Wed Sep 30 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-3
- run find on the right directory

* Tue Sep 29 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-2
- remove executable bits from docs
- remove defattr line

* Sat Sep 26 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-1
- update to 1.7.1

* Thu Sep 10 2015 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-7
- use python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-5
- fix mupdf binary name (rhbz#1186823)

* Sat Dec 13 2014 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-4
- Fix the right file (was the source file, but upstream regenerates the
  installed file manually).

* Thu Dec 11 2014 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-3
- Fix documentation typo

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- add rifle command

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Ben Boeckel <mathstuf@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Jul 24 2010 Ben Boeckel <mathstuf@gmail.com> - 1.1.2-2
- Add patch to remove shebang line
- BR python2-devel

* Fri Jul 23 2010 Ben Boeckel <mathstuf@gmail.com> - 1.1.2-1
- Initial package
