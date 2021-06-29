%global pypi_name smartypants

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        3%{?dist}
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities

License:        BSD
URL:            https://github.com/leohemsted/smartypants.py
Source0:        %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.


%package -n python-%{pypi_name}-doc
Summary:        python-smartypants documentation
%description -n python-%{pypi_name}-doc
Documentation for python-smartypants


%prep
%autosetup -n %{pypi_name}.py-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
for lib in $(find -type f -name '*.py'); do
 sed -i.python -e '1{\@^#!@d}' $lib
done
sed -i.python -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' smartypants


%build
%py3_build
# generate html documentation
cd docs
make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}


%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%doc README.rst
%doc CHANGES.rst
%license COPYING
%{_bindir}/%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc docs/_build/html
%license COPYING

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 2.0.1-2
- fix source url, license short hand, description and summary.
- remove shebang lines and make smartypants a shebang line use python3.

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 2.0.1-1
- initial package.
