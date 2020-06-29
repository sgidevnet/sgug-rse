%global pypi_name pymeeus

Name:           python-%{pypi_name}
Version:        0.3.6
Release:        4%{?dist}
Summary:        Python implementation of Jean Meeus astronomical routines

License:        LGPLv3
URL:            https://github.com/architest/pymeeus
Source0:        %{pypi_source PyMeeus}
BuildArch:      noarch

%description
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book "Astronomical Algorithms, 2nd Edition, Willmann-Bell
Inc. (1998)" by Jean Meeus.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book "Astronomical Algorithms, 2nd Edition, Willmann-Bell
Inc. (1998)" by Jean Meeus.

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n PyMeeus-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt COPYING.LESSER
%doc docs/README.txt README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/PyMeeus-%{version}-py*.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt COPYING.LESSER

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-2
- Use var for source URL
- Split BRs
- Delete hidden files from doc generation
- Better use of wildcards (rhbz#1787140)

* Tue Dec 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Initial package for Fedora
