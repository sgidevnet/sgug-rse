%global modname cerberus

Name:           python-%{modname}
Version:        1.3.1
Release:        5%{?dist}
Summary:        Lightweight, extensible data validation library for Python

License:        ISC
URL:            https://github.com/pyeve/cerberus
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
Patch1:         %{url}/pull/507.patch

BuildArch:      noarch

%global _description \
Cerberus is a lightweight and extensible data validation library for Python.\
\
Cerberus provides type checking and other base functionality out of the box\
and is designed to be non-blocking and easily extensible, allowing for custom\
validation. It has no dependancies and is thoroughly tested.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v %{modname}/tests

%files -n python3-%{modname}
%license LICENSE
%doc README.rst AUTHORS CHANGES.rst
%{python3_sitelib}/Cerberus-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.8

* Sun Jul 28 16:42:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-3
- Subpackage python2-cerberus has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-2
- Enable python dependency generator

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-1
- Update to 1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-1
- Update to 1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuild for Python 3.6

* Thu Sep 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-1
- Initial package
