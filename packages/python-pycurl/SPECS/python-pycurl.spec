# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

# python3 is not available on RHEL <= 7
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

# python2 is not available on RHEL > 7
%if 0%{?rhel} > 7
%bcond_with python2
%else
%bcond_without python2
%endif

%bcond_without python3
%bcond_without python2

%global modname pycurl

Name:           python-%{modname}
Version:        7.43.0.2
Release:        7%{?dist}
Summary:        A Python interface to libcurl

License:        LGPLv2+ or MIT
URL:            http://pycurl.sourceforge.net/
Source0:        https://dl.bintray.com/pycurl/pycurl/pycurl-%{version}.tar.gz

# fix programming mistakes detected by static analyzers
# upstream pull request: https://github.com/pycurl/pycurl/pull/550
Patch1:         0001-python-pycurl-7.43.0.2-static-analysis.patch

# drop link-time vs. run-time TLS backend check (#1446850)
Patch2:         0002-python-pycurl-7.43.0-tls-backend.patch

Patch100:       pycurl.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
#BuildRequires:  vsftpd

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
#%%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;q'
%global curlver_h /usr/include/curl/curlver.h
#%%global libcurl_ver %%(sed %%{libcurl_sed} %%{curlver_h} 2>/dev/null || echo 0)
%global libcurl_ver 7.61.0

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%if %{with python2}
%package -n python2-%{modname}
Summary:        Python interface to libcurl for Python 2
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-bottle
BuildRequires:  python2-nose
BuildRequires:  python2-pyflakes
Requires:       libcurl%{?_isa} >= %{libcurl_ver}

Provides:       %{modname} = %{version}-%{release}

%description -n python2-%{modname}
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

Python 2 version.
%endif

%if %{with python3}
%package -n python3-%{modname}
Summary:        Python interface to libcurl for Python 3
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-bottle
BuildRequires:  python3-nose
BuildRequires:  python3-pyflakes
Requires:       libcurl%{?_isa} >= %{libcurl_ver}

%description -n python3-%{modname}
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

Python 3 version.
%endif

%prep
%autosetup -n %{modname}-%{version} -p1

# remove binaries packaged by upstream
rm -f tests/fake-curl/libcurl/*.so

# remove a test-case that relies on sftp://web.sourceforge.net being available
rm -f tests/ssh_key_cb_test.py

# remove a test-case that fails in Koji
rm -f tests/seek_cb_test.py

# remove tests depending on the 'flaky' nose plug-in (not available in Fedora)
grep '^import flaky' -r tests | cut -d: -f1 | xargs rm -fv

# drop options that are not supported by nose in Fedora
%{_bindir}/sed -e 's/ --show-skipped//' \
    -e 's/ --with-flaky//' \
    -i tests/run.sh

# A place to generate the patch
#exit 1

%build
%if %{with python2}
%py2_build '--with-openssl'
%endif
%if %{with python3}
%py3_build '--with-openssl'
%endif

%install
export PYCURL_SSL_LIBRARY=openssl
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%if %{with python3}
%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYCURL_SSL_LIBRARY=openssl
#export PYCURL_VSFTPD_PATH=vsftpd
make test PYTHON=%{__python3} NOSETESTS="nosetests-%{python3_version} -v"
rm -fv tests/fake-curl/libcurl/*.so
%endif

%if %{with python2}
%files -n python2-%{modname}
%license COPYING-LGPL COPYING-MIT
%doc ChangeLog README.rst examples doc tests
%{python2_sitearch}/curl/
%{python2_sitearch}/%{modname}.so
%{python2_sitearch}/%{modname}-%{version}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{modname}
%license COPYING-LGPL COPYING-MIT
%doc ChangeLog README.rst examples doc tests
%{python3_sitearch}/curl/
%{python3_sitearch}/%{modname}.*.so
%{python3_sitearch}/%{modname}-%{version}-*.egg-info
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.43.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Kamil Dudka <kdudka@redhat.com> - 7.43.0.2-6
- reintroduce the python2-pycurl subpackage on Fedora (#1672061)
