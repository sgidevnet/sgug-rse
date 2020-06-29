%global pypi_name hkdf

%global common_description %{expand:
This module implements the HMAC Key Derivation function, defined at
http://tools.ietf.org/html/draft-krawczyk-hkdf-01. There are two
interfaces: a functional interface, with separate extract and expand
functions as defined in the draft RFC, and a wrapper class for these
functions.}

Name:           python-%{pypi_name}
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
Version:        0.0.3
Release:        7%{?dist}
License:        BSD

URL:            https://github.com/casebeer/python-hkdf
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst

%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.0.3-1
- Initial package.

