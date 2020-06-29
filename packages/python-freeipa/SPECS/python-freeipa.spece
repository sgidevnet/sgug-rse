# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global pypi_name python-freeipa
%global srcname freeipa

Name:           python-%{srcname}
Version:        1.0.4
Release:        2%{?dist}
Summary:        Lightweight FreeIPA client

License:        MIT
URL:            https://python-freeipa.readthedocs.io/
Source0:        https://github.com/opennode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist responses}
BuildRequires:  %{py3_dist setuptools}

%description
python-freeipa is lightweight FreeIPA client.

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary} for Python %{python3_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
python-freeipa is lightweight FreeIPA client.

This package provides the Python %{python3_version} variant.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%python3 setup.py test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/python_freeipa/
%{python3_sitelib}/python_freeipa-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.9

* Tue Apr 21 19:45:43 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.4-1
- Update to 1.0.4 (#1826547)

* Fri Apr 17 15:22:42 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.3-1
- Update to 1.0.3 (#1825360)

* Mon Apr 13 10:26:54 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.2-1
- Initial package for Fedora (#1823091)
