%{?python_enable_dependency_generator}
%bcond_without check

%global modname pynacl

Name:           python-%{modname}
Version:        1.3.0
Release:        8%{?dist}
Summary:        Python binding to the Networking and Cryptography (NaCl) library

License:        ASL 2.0
URL:            https://github.com/pyca/pynacl
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

# hypothesis 4 support
Patch1:         %{url}/pull/480.patch

# hypothesis 5 support
Patch2:         %{url}/pull/572.patch

BuildRequires:  gcc
BuildRequires:  libsodium-devel

%global _description \
PyNaCl is a Python binding to the Networking and Cryptography library,\
a crypto library with the stated goal of improving usability, security\
and speed.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi >= 1.4.1
%if %{with check}
BuildRequires:  python3-six
BuildRequires:  python3-pytest >= 3.2.1
BuildRequires:  python3-hypothesis >= 3.27.0
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Remove bundled libsodium, to be sure
rm -vrf src/libsodium/

# ARM and s390x is too slow for upstream tests
# See https://bugzilla.redhat.com/show_bug.cgi?id=1594901
# And https://github.com/pyca/pynacl/issues/370
%ifarch s390x %{arm}
sed -i 's/@settings(deadline=1500, max_examples=5)/@settings(deadline=4000, max_examples=5)/' tests/test_pwhash.py
%endif

%build
export SODIUM_INSTALL=system
%py3_build

%install
%py3_install

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -v
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/PyNaCl-*.egg-info/
%{python3_sitearch}/nacl/

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-8
- Rebuilt for Python 3.9

* Mon May 11 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Fix build with hypothesis 5 (#1830961)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Subpackage python2-pynacl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Yatin Karel <ykarel@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.7
- Prolong the deadline for tests on s390x
- Don't ignore the test results on arm, do the same as on s390x

* Tue Mar 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 1.1.2-4
- rebuild for libsodium

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Thu Mar 16 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Initial package
