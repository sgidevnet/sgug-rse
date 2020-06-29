%global srcname zarr

Name:           python-%{srcname}
Version:        2.4.0
Release:        2%{?dist}
Summary:        Chunked, compressed, N-dimensional arrays for Python

License:        MIT
URL:            https://github.com/zarr-developers/zarr
Source0:        %{pypi_source}
# https://github.com/zarr-developers/zarr/pull/442
Patch0001:      0001-Explicitly-close-stores-during-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asciitree)
BuildRequires:  python3dist(bsddb3)
BuildRequires:  python3dist(fasteners)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(lmdb)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(numcodecs) >= 0.5.3
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) > 18
BuildRequires:  python3dist(setuptools-scm) > 1.5.4

%description
Zarr is a Python package providing an implementation of compressed, chunked,
N-dimensional arrays, designed for use in parallel computing.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Zarr is a Python package providing an implementation of compressed, chunked,
N-dimensional arrays, designed for use in parallel computing.


%package -n python-%{srcname}-doc
Summary:        zarr documentation

BuildArch:      noarch

BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python-%{srcname}-doc
Documentation for zarr


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo,_static/donotdelete}


%install
%py3_install


%check
%{__python3} -m pytest


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.2-2
- Fix tests on 32-bit arches

* Thu May 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.2-1
- Update to latest version

* Tue Apr 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-2
- Fix tests on big-endian arches

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-1
- Update to latest version

* Mon Mar 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-2
- Fix test running
- Make doc subpackage noarch

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Initial package.
