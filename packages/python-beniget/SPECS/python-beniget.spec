%global pypi_name beniget

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        3%{?dist}
Summary:        Extract semantic information about static Python code

License:        BSD
URL:            https://github.com/serge-sans-paille/beniget/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-gast >= 0.3
BuildRequires:  python3-setuptools

%description
A static analyzer for Python2 and Python3 code.Beniget provides a static over-
approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each definition.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A static analyzer for Python2 and Python3 code.Beniget provides a static over-
approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each definition.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- Initial package
