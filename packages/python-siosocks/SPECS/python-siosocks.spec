%global pypi_name siosocks

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        4%{?dist}
Summary:        Sans-io socks proxy client/server with couple io backends

License:        MIT
URL:            https://github.com/pohmelie/siosocks
Source0:        %{pypi_source}
BuildArch:      noarch

%description
socks 4/5 client/server library/framework.

- No one-shot socks servers
- Sans-io
- asyncio-ready

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-trio
BuildRequires:  python3-setuptools
BuildRequires:  python3-trio
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
socks 4/5 client/server library/framework.

- No one-shot socks servers
- Sans-io
- asyncio-ready

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license license.txt
%doc readme.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-2
- Use var for source URL
- Better use of wildcards (rhbz#1787309)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
