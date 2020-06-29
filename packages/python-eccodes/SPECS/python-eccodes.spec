Name:           python-eccodes
Version:        0.9.7
Release:        2%{?dist}
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder
License:        ASL 2.0
URL:            https://pypi.org/project/eccodes-python/
Source0:        https://files.pythonhosted.org/packages/source/e/eccodes-python/eccodes-python-%{version}.tar.gz
# see https://github.com/ecmwf/eccodes-python/pull/21
Patch1:         python-eccodes-setup.patch

# note that the fast bindings are arch dependent
BuildRequires:  eccodes-devel
BuildRequires:  python3-devel
# needed to build the fast bindings
BuildRequires:  python3-cffi
# needed for checks/tests
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
# these next 2 seem not actually used, although they are mentioned as
# test dependencies in the setup.py file:
#BuildRequires:  python3-pytest-cov
#BuildRequires:  python3-pytest-flakes

# needed to build the documentation
BuildRequires:  python3-sphinx

# dont try to build for architectures for which the main
# ecccodes library cannot yet be build

# as explained in bugzilla #1562066
ExcludeArch: i686
# as explained in bugzilla #1562076
ExcludeArch: s390x
# as explained in bugzilla #1562084
ExcludeArch: armv7hl


%global _description \
Python 3 interface to encode and decode GRIB and BUFR files via the \
ECMWF ecCodes library. It allows reading and writing of GRIB 1 and 2 \
files and BUFR 3 and 4 files.

%description %_description

%package -n python3-eccodes
Summary: %summary

%{?python_provide:%python_provide python3-eccodes}

%description -n python3-eccodes %_description

%prep
%autosetup -n eccodes-python-%{version} -p1

%build
%py3_build
# buld documentation
%{__python3} setup.py build_sphinx
# remove generated sphinx files that are not part of the actual documentation
rm build/sphinx/html/.buildinfo

%install
%py3_install

# remove *.h files that do not belong in a python module directory
rm %{buildroot}%{python3_sitearch}/gribapi/*.h

%check
%{__python3} -m eccodes selfcheck
%{__python3} -m pytest -v

%files -n python3-eccodes
%doc README.rst
%doc build/sphinx/html/
%license LICENSE
%{python3_sitearch}/eccodes_python-*-py*.egg-info
%{python3_sitearch}/eccodes
%{python3_sitearch}/gribapi


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Jos de Kloe <josdekloe@gmail.com> 0.9.7-1
- First version for Fedora, based on a spec file contributed by
  Emanuele Di Giacomo and Daniele Branchini.
