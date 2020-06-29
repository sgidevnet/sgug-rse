%global srcname readthedocs-sphinx-ext

Name:           python-%{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Sphinx extension for Read the Docs overrides

License:        MIT
URL:            https://github.com/readthedocs/readthedocs-sphinx-ext
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros

# upstream supports multiple sphinx versions
# tox specifies dependency on sphinx based on toxenv,
# so we add it manually here
BuildRequires:  python3dist(sphinx)

%global _desc %{expand:
This module adds extensions that make Sphinx easier to use.  Some of them
require Read the Docs features, others are just code that we ship and
enable during builds on Read the Docs.  We currently ship:
- An extension for building docs like Read the Docs
- template-meta - allows users to specify template overrides in per-page
  contexts.}

%description %_desc

%package -n     python3-%{srcname}
Summary:        Sphinx extension for Read the Docs overrides

%description -n python3-%{srcname} %_desc

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%doc README.html
%license LICENSE
%{python3_sitelib}/readthedocs_ext/
%{python3_sitelib}/readthedocs_sphinx_ext*

%changelog
* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-2
- Remove unnecessary version manipulation

* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Thu Jan 30 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
