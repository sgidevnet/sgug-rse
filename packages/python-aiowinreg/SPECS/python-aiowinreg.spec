%global pypi_name aiowinreg

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        2%{?dist}
Summary:        Windows registry file reader

License:        MIT
URL:            https://github.com/skelsec/aiowinreg
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/skelsec/aiowinreg/master/LICENSE
BuildArch:      noarch

%description
Windows registry file reader.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Windows registry file reader.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-1
- Update to latest upstream release 0.0.3 (rhbz#1815001)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Initial package for Fedora
