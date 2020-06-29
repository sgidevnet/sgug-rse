Name:           python-fiat
Version:        2019.1.0
Release:        4%{?dist}
Summary:        Generator of arbitrary order instances of Lagrange elements on lines, triangles, and tetrahedra
%global data_version 83d6c1d8f30d

Source0:        https://bitbucket.org/fenics-project/fiat/downloads/fiat-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/fiat/downloads/fiat-%{version}.tar.gz.asc
Source2:        https://bitbucket.org/fenics-project/fiat-reference-data/get/%{data_version}.zip#/fiat-reference-data-%{data_version}.zip

Patch0001:      https://bitbucket.org/fenics-project/fiat/commits/852a15f1a21e360cde3bc8b53693dc933712806e/raw#/patch0001.patch
Patch0002:      https://bitbucket.org/fenics-project/fiat/commits/b8e9c1e64264bd2a0276db483ab300f7c16bf8e2/raw#/patch0002.patch
Patch0004:      https://bitbucket.org/fenics-project/fiat/commits/3b17d82a5678746234247bad3b9c019f49bc00ad/raw#/patch0004.patch
Patch0005:      https://bitbucket.org/fenics-project/fiat/commits/1d0f416f3b3093ccf72ff8cc65a56a213abbbd43/raw#/patch0005.patch

License:        LGPLv3+
URL:            https://bitbucket.org/fenics-project/fiat
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cases)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(sympy)
BuildRequires:  /usr/bin/unzip

%global _description %{expand:
The FInite element Automatic Tabulator FIAT supports generation of
arbitrary order instances of the Lagrange elements on lines,
triangles, and tetrahedra. It is also capable of generating arbitrary
order instances of Jacobi-type quadrature rules on the same element
shapes. Further, H(div) and H(curl) conforming finite element spaces
such as the families of Raviart-Thomas, Brezzi-Douglas-Marini and
Nedelec are supported on triangles and tetrahedra. Upcoming versions
will also support Hermite and nonconforming elements.

FIAT is part of the FEniCS Project.}

%description %_description

%package -n python3-fiat
Summary: %summary
%{?python_provides python3-fiat}

%description -n python3-fiat %_description

%prep
%autosetup -n fiat-%{version} -p1
cd test/regression
unzip %{SOURCE2}
ln -s fenics-project-fiat-reference-data-%{data_version} fiat-reference-data

%build
%py3_build

%install
%py3_install

%check
%__python3 -m pytest -v test/ --skip-download

%files -n python3-fiat
%license COPYING
%license COPYING.LESSER
%doc README.rst
%doc AUTHORS
%{python3_sitelib}/FIAT/
%{python3_sitelib}/fenics_fiat-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2019.1.0-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Fabian Affolter <mail@fabian-affolter.ch> 2018.1.0-1
- Update to latest upstream release 2018.1.0
- Python 2 is no longer supported

* Sun Sep 09 2018 Jan Beran <jberan@redhat.com> - 1.6.0-12
- Fix missing Python 3 version of executables (rhbz#1436805)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Oct 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 1.6.0-2
- Remove unneeded PythonScientific dependency
- Convert to modern python packaging format and add python3 subpackage

* Sun Oct 11 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update to new upstream 1.6.0 (rhbz#1247601)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0.-1
- Update to new upstream 1.6.0 (rhbz#1247601)

* Thu Jul 31 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0.-1
- Spec file update
- Update to new upstream 1.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 24 2013 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1.0-1
- Update to version 1.1.0
- Fix the BuildRequires for LaTeX for F18 and beyond

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0.0-3
- Add Requires: ScientificPython

* Thu May  3 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.0.0-2
- Build PDF of the manual
- Move executable scripts to %%{_bindir}

* Sat Feb 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0.-1
- Update to new upstream 1.0.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Update URL and description
- Update to new upstream version 0.9.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Update to new upstream version 0.9.2
- Update source url

* Tue Feb 23 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Change source URL
- Add docs
- Update to new upsteram version 0.9.1

* Sun Dec 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to new upsteram version 0.3.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-2
- Fix license tag -> LGPLv2+

* Fri Jan 30 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Initial package for Fedora
