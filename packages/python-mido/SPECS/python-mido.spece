%global pypi_name mido

Name:           python-%{pypi_name}
Version:        1.2.9
Release:        7%{?dist}
Summary:        A Python library for working with MIDI messages and ports

License:        MIT
URL:            https://mido.readthedocs.io/
Source0:        https://github.com/mido/mido/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Mido is a library for working with MIDI messages and ports.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Mido is a library for working with MIDI messages and ports.

%package -n python-%{pypi_name}-doc
Summary:        sphinxcontrib-asyncio documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

# Tests require dependencies which are not available at the moment
#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/mido-*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.9-5
- Add docs

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.9-1
- Initial package for Fedora
