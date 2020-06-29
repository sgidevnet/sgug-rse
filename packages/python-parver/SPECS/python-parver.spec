%global pypi_name parver
Name:           python-%{pypi_name}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Parse and manipulate version numbers

License:        MIT
URL:            https://github.com/RazerM/parver
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(arpeggio)
BuildRequires:  python3dist(attrs) >= 17.4
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%?python_enable_dependency_generator

%description
Parver allows parsing and manipulation of PEP 440 version numbers.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parver allows parsing and manipulation of PEP 440 version numbers.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Initial package
