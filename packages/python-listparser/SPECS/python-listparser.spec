# Created by pyp2rpm-3.3.2
%global pypi_name listparser

Name:           python-%{pypi_name}
Version:        0.18
Release:        6%{?dist}
Summary:        Parse OPML, FOAF, and iGoogle subscription lists

License:        LGPLv3+
URL:            https://github.com/kurtmckee/listparser
Source0:        %pypi_source
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
listparser is a Python library that parses subscription lists (also called
reading lists) and returns all of the feeds, subscription lists, and
"opportunity" URLs that it finds. It supports OPML, RDF+FOAF, and the iGoogle
exported settings format.

%package -n python-%{pypi_name}-doc
Summary:        listparser documentation
%description -n python-%{pypi_name}-doc
Documentation for listparser.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
chmod 644 COPYING
chmod 644 COPYING.LESSER
chmod 644 README.rst

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} lptest.py test

%files -n python3-%{pypi_name}
%license COPYING COPYING.LESSER
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%license COPYING COPYING.LESSER
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18-3
- Initial package
