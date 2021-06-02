%global srcname ECPy
%global owner cslashm
%global desc ECPy (pronounced ekpy), is a pure python Elliptic Curve library \
providing ECDSA, EDDSA, ECSchnorr, Borromean signatures as well as Point \
operations.

Name:     python-%{srcname}
Version:  0.10.0
Release:  3%{?dist}
Summary:  Python Elliptic Curve Library

License:  ASL 2.0
URL:      https://github.com/%{owner}/%{srcname}
Source0:  https://github.com/%{owner}/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-sphinx

%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary: Documentation for python-%{srcname}

%description doc
This package contains the documentation for python-%{srcname}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
%make_build -C doc singlehtml
rm -f doc/build/singlehtml/{.buildinfo,.nojekyll}


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%files doc
%license LICENSE
%doc doc/build/singlehtml/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0
- Upstream repo changed ownership from ubinity -> cslashm

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.2-6
- Subpackage python2-ECPy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 9 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.8.1-1
- Initial packaging for Fedora
