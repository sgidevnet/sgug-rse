%global modname semver

Name:           python-%{modname}
Version:        2.8.1
Release:        7%{?dist}
Summary:        Python helper for Semantic Versioning

License:        BSD
URL:            https://github.com/k-bx/python-semver
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Python module for semantic versioning. Simplifies comparing versions.

%description %{_description}

%package     -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst CHANGELOG
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.8-1
- Update to 2.7.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.7-1
- Update to 2.7.7

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.5-1
- Update to 2.7.5

* Sat Jan 28 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.4-1
- Initial package
