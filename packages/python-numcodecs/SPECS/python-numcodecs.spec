%global srcname numcodecs

Name:           python-%{srcname}
Version:        0.6.4
Release:        3%{?dist}
Summary:        Buffer compression and transformation for data storage and communication

License:        MIT
URL:            https://github.com/alimanfoo/numcodecs
Source0:        %{pypi_source}
# Fedora specific
Patch0001:      0001-Unbundle-blosc.patch
Patch0002:      0002-Unbundle-zstd.patch
Patch0003:      0003-Unbundle-lz4.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools) > 18
BuildRequires:  python3dist(setuptools-scm) > 1.5.4

%description
Numcodecs is a Python package providing buffer compression and transformation
codecs for use in data storage and communication applications.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Numcodecs is a Python package providing buffer compression and transformation
codecs for use in data storage and communication applications.


%package -n python-%{srcname}-doc
Summary:        numcodecs documentation

BuildArch:      noarch

BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-issues)

%description -n python-%{srcname}-doc
Documentation for numcodecs


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove bundled blosc
rm -rf c-blosc


%build
%py3_build

# generate html docs
PYTHONPATH=$(ls -d build/lib*) sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo} html/_static/donotdelete


%install
%py3_install


%check
cd docs  # Avoid using unbuilt existing copy.
ln -s ../fixture
PYTHONPATH=%{buildroot}%{python3_sitearch} PYTHONDONTWRITEBYTECODE=1 \
    %{__python3} -m pytest --pyargs numcodecs


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.4-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-3
- Fix build against latest NumPy

* Mon Mar 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-2
- Fix broken doc build and test running
- Make doc subpackage noarch

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Initial package.
