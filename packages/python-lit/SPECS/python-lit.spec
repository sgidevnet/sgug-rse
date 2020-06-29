%global srcname lit

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

#%%global rc_ver 1
%global baserelease 3

%bcond_without check

# FIXME: Work around for rhel not having py2_build/py2_install macro.
%{!?py2_build: %global py2_build %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} build --executable="%{__python2} -s"}}
%{!?py2_install: %global py2_install %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot}}}

Name: python-%{srcname}
Version: 0.10.0
Release: %{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
BuildArch: noarch

License: NCSA
Summary: Tool for executing llvm test suites
URL: https://pypi.python.org/pypi/lit
Source0: https://files.pythonhosted.org/packages/e7/56/7967ff7ea510c12a4f3d5f6582a416ff74bd6b1194be265c979df6701c56/lit-0.10.0.tar.gz

Patch0: version.patch

# for file check
%if %{with check}
BuildRequires: llvm-test
%endif

BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if 0%{?with_python2}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
%endif

%description
lit is a tool used by the LLVM project for executing its test suites.

%package -n python3-lit
Summary: LLVM lit test runner for Python 3

Requires: python3-setuptools

%if 0%{?with_python2}
%package -n python2-lit
Summary: LLVM lit test runner for Python 2

Requires: python2-setuptools
%endif

%description -n python3-lit
lit is a tool used by the LLVM project for executing its test suites.

%if 0%{?with_python2}
%description -n python2-lit
lit is a tool used by the LLVM project for executing its test suites.
%endif

%prep
%autosetup -n %{srcname}-%{version}%{?rc_ver:rc%{rc_ver}} -p4

%build
%py3_build
%if 0%{?with_python2}
%py2_build
%endif

%install
%py3_install
%if 0%{?with_python2}
%py2_install
%endif

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{srcname}/*.py
%if 0%{?with_python2}
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python2_sitelib}/%{srcname}/*.py
%endif

%if %{with check}
%check
%{__python3} lit.py tests
%if 0%{?with_python2}
%{__python2} lit.py tests
%endif
%endif

%files -n python3-%{srcname}
%doc README.txt
%{python3_sitelib}/*
%{_bindir}/lit

%if 0%{?with_python2}
%files -n python2-%{srcname}
%doc README.txt
%{python2_sitelib}/*
%if %{undefined with_python2}
%{_bindir}/lit
%endif
%endif

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Bootstrap for Python 3.9

* Thu Apr 9 2020 sguelton@redhat.com - 0.10.0-1
- 0.10.0 final release

* Tue Feb 11 2020 sguelton@redhat.com - 0.10.0-0.1.rc1
- 0.10.0 rc1 Release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-3
- Re-enable tests

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-2
- Disable check to avoid circular dependency with llvm-test

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-1
- 0.9.0 Release

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-0.1.rc4
- 0.9.0 rc4 Release

* Tue Aug 20 2019 sguelton@redhat.com - 8.0.0-7
- Rebuild for Python 3.8 with test, preparatory work for rhbz#1715016

* Tue Aug 20 2019 sguelton@redhat.com - 8.0.0-6
- Rebuild for Python 3.8 without test, preparatory work for rhbz#1715016

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 sguelton@redhat.com - 8.0.0-3
- Fix rhbz#1728067

* Fri Jun 28 2019 sguelton@redhat.com - 8.0.0-2
- Fix rhbz#1725155

* Thu Mar 21 2019 sguelton@redhat.com - 8.0.0-1
- 0.8.0 Release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 sguelton@redhat.com - 0.7.1-1
- 7.0.1 Release

* Tue Sep 25 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-2
- Add missing dist to release tag

* Fri Sep 21 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-1
- 0.7.0 Release

* Fri Aug 31 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-0.2.rc1
- Add Requires: python[23]-setuptools

* Mon Aug 13 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-0.1.rc1
- 0.7.0 rc1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-1
- 0.6.0 Release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-0.1.rc1
- 0.6.0 rc1

* Tue Jan 23 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-4
- Add a missed python3 conditional around a sed operation

* Mon Jan 15 2018 Merlin Mathesius <mmathesi@redhat.com> - 0.5.1-3
- Cleanup spec file conditionals

* Wed Dec 06 2017 Tom Stellard <tstellar@redhat.com> - 0.5.1-2
- Fix python prefix in BuildRequires

* Tue Oct 03 2017 Tom Stellard <tstellar@redhat.com> - 0.5.1-1
- Rebase to 0.5.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-1
- Initial version
