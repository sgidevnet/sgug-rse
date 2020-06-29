%global srcname mercantile

Name:           python-%{srcname}
Version:        1.1.5
Release:        1%{?dist}
Summary:        Web Mercator XYZ tile utilities

License:        BSD
URL:            https://github.com/mapbox/mercantile
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(check-manifest)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(numpydoc)

%global _description %{expand:\
Mercantile is a module of utilities for working with XYZ style Spherical
Mercator tiles (as in Google Maps, OSM, Mapbox, etc.) and includes a set of
command line programs built on these utilities.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{buildinfo,doctrees}

%install
%py3_install

%check
pytest-3

%files -n python3-%{srcname}
%doc README.rst html
%license LICENSE.txt
%{_bindir}/mercantile
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Sun Jun 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.5-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version

* Tue Apr 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Update to latest version

* Thu Feb 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.2-1
- Initial package.
