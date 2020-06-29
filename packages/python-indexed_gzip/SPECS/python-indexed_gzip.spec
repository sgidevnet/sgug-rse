# tests are not meant to be run against installed version, says upstream.
# confirmed that they work with python setup.py develop
# https://github.com/pauldmccarthy/indexed_gzip/issues/13
%global with_tests 0

%global srcname indexed_gzip

%global desc %{expand: \
The indexed_gzip project is a Python extension which aims to provide a drop-in
replacement for the built-in Python gzip.GzipFile class, the IndexedGzipFile.

indexed_gzip was written to allow fast random access of compressed NIFTI image
files (for which GZIP is the de-facto compression standard), but will work with
any GZIP file.  indexed_gzip is easy to use with nibabel.

The standard gzip.GzipFile class exposes a random access-like interface (via
its seek and read methods), but every time you seek to a new point in the
uncompressed data stream, the GzipFile instance has to start decompressing from
the beginning of the file, until it reaches the requested location.

An IndexedGzipFile instance gets around this performance limitation by building
an index, which contains *seek points*, mappings between corresponding
locations in the compressed and uncompressed data streams. Each seek point is
accompanied by a chunk (32KB) of uncompressed data which is used to initialise
the decompression algorithm, allowing us to start reading from any seek point.
If the index is built with a seek point spacing of 1MB, we only have to
decompress (on average) 512KB of data to read from any location in the file.}


Name:           python-%{srcname}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Fast random access of gzip files in Python


License:        zlib
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  zlib-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
# remove wrong interpreter
find . -name "*py" -exec sed -i '/^#!\/usr\/bin\/env python/ d' '{}' \;
rm -rfv %{srcname}.egg-info
# Remove cythonised c files so that they are regenerate
rm -fv %{srcname}/{indexed_gzip}.c
rm -fv %{srcname}/tests/ctest_{indexed_gzip}.c

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
pytest-%{python3_version} .
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{srcname}

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-1
- Update to 1.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.10-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.10-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.10-2
- Remove cythonised sources

* Fri May 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.10-1
- Update to newest release
- rhbz: 1710384

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.8-1
- Update to latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.7-1
- Initial build
