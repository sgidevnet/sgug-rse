%global srcname cppy

Name:           python-%{srcname}
Version:        1.1.0
Release:        2%{?dist}
Summary:        C++ headers for C extension development

License:        BSD
URL:            https://github.com/nucleic/cppy
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.


%package -n python-%{srcname}-doc
Summary:        cppy documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for cppy


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    pytest-3 tests


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Initial package.
