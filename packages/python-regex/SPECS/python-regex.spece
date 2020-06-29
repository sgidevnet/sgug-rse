%global srcname regex

Name:           python-%{srcname}
Version:        2020.6.8
Release:        2%{?dist}
Summary:        Alternative regular expression module, to replace re
# see also https://code.google.com/p/mrab-regex-hg/issues/detail?id=124
License:        Python and CNRI
URL:            https://bitbucket.org/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  %{_bindir}/rst2html
BuildRequires:  gcc


%description
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Alternative regular expression module, to replace re
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.


%prep
%autosetup -n %{srcname}-%{version}

# will be rebuilt
rm docs/Features.html


%build
%py3_build
# rebuild the HTML doc
rst2html docs/Features.rst > docs/Features.html
rst2html docs/UnicodeProperties.rst > docs/UnicodeProperties.html
rst2html README.rst > README.html


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.html
%doc docs/Features.html
%doc docs/UnicodeProperties.html
%{python3_sitearch}/*


%changelog
* Sat Jun 20 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.6.8-2
- Update to 2020.6.8.

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.5.14-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.5.14-1
- Update to 2020.5.14.

* Tue Apr 14 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.4.4-1
- Update to 2020.4.4.

* Sat Feb 22 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.2.20-1
- Update to 2020.2.20.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2020.1.8-1
- Update to 2020.1.8.

* Fri Jan  3 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.20-2
- Add BR on setuptools.

* Wed Jan  1 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.20-1
- Update to 2019.12.20.
- Update doc generation.

* Sat Dec 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.12.9-1
- Update to 2019.12.9.

* Sat Nov  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.11.1-1
- Update to 2019.11.1.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.08.19-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.08.19-2
- Remove Python2 subpackage (bz#1744656).

* Tue Aug 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.08.19-1
- Update to 2019.08.19.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.06.08-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.06.08-1
- Update to 2019.06.08.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.05.25-1
- Update to 2019.05.25.

* Mon Apr 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.04.14-1
- Update to 2019.04.14.

* Sat Mar  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.03.09-1
- Update to 2019.03.09.

* Sat Feb  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.02.07-1
- Update to 2019.02.07.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2019.01.24-1
- Update to 2019.01.24.

* Tue Dec 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.11.22-1
- Update to 2018.11.22.

* Sun Nov 11 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.11.07-1
- Update to 2018.11.07.

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.07.11-1
- Update to 2018.07.11.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06.21-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.21-1
- Update to 2018.06.21.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06.09-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.09-1
- Update to 2018.06.09.

* Wed Jun  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.06.06-1
- Update to 2018.06.06.

* Sun Mar  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.21-1
- Update to 2018.02.21.

* Sun Feb 11 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.08-1
- Update to 2018.02.08.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.02.03-1
- Update to 2018.02.03.

* Sat Jan 13 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2018.01.10-1
- Update to 2018.01.10.

* Sat Nov 18 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2017.11.09-1
- Update to 2017.11.09.
- Build Python3 subpackage on EPEL7.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.09.22-2
- Rebuild for Python 3.6

* Sat Sep 24 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.09.22-1
- Update to 2016.09.22.

* Sun Aug  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.07.21-1
- Update to 2016.07.21.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.06.24-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.24-1
- Update to 2016.06.24.

* Mon Jun 13 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.05-1
- Update to 2016.06.05.

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.02-1
- Update to 2016.06.02.
- Update upstream URL.

* Mon May 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.05.23-1
- Update to 2016.05.23.

* Fri Apr 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.25-1
- Update to 2016.04.25.

* Sat Apr  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.08-1
- Update to 2016.04.08.
- Update upstream URL.

* Tue Apr  5 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.02-1
- Update to 2016.04.02.

* Mon Mar  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.03.02-2
- Update to 2016.03.02.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2016.01.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.01.10-1
- Update to 2016.01.10.

* Sun Dec 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.11.22-1
- Update to 2015.11.22.
- Follow updated Python packaging guidelines.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.07.19-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.07.19-1
- Update to 2015.07.19.

* Thu Jun 25 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.06.24-1
- Update to 2015.06.24.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.05.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.28-1
- Update to 2015.05.28.

* Sat May 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.10-1
- Update to 2015.05.10.

* Sat Mar 21 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.03.18-1
- Update to 2015.03.18.
- Apply updated Python packaging guidelines.

* Thu Jan  8 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.24-1
- Update to 2014.12.24.

* Sun Dec 21 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.15-1
- Update to 2014.12.15.

* Sat Dec 13 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.11.14-1
- Update to 2014.11.14.
- Rebuild the HTML docs.
- Update License tag.
- Update upstream URL.

* Wed Oct 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.10.09-1
- Initial version.
