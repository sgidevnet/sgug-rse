%global srcname mapclassify

Name:           python-%{srcname}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Classification Schemes for Choropleth Maps

License:        BSD
URL:            https://github.com/pysal/mapclassify
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(deprecated)
BuildRequires:  python3dist(numpy) >= 1.3
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy) >= 0.11
BuildRequires:  python3dist(setuptools)

# Tests
BuildRequires:  python3dist(geopandas)
BuildRequires:  python3dist(libpysal)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(nose-exclude)
BuildRequires:  python3dist(nose-progressive)

# Docs
#BuildRequires:  python3dist(numpydoc)
#BuildRequires:  python3dist(sphinx) >= 1.4.3
#BuildRequires:  python3dist(sphinx-bootstrap-theme)
#BuildRequires:  python3dist(sphinx-gallery)
#BuildRequires:  python3dist(sphinxcontrib-bibtex)

%description
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove extra files
# https://github.com/pysal/mapclassify/issues/56
rm %{srcname}/deprecation.py
rm "%{srcname}/flycheck_classifiers (serges-MacBook-Pro.local's conflicted copy 2019-07-03).py"
rm %{srcname}/test.py


%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.9

* Thu Feb 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Initial package.
