
Name:           python-cccolutils
Version:        1.5
Release:        15%{?dist}
Summary:        Python Kerberos Credential Cache Collection Utilities

License:        GPLv2+
URL:            https://pagure.io/cccolutils
Source0:        https://pagure.io/releases/cccolutils/CCColUtils-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Python utilities for Kerberos Credential Cache Collections


%package     -n python3-cccolutils
Summary:        Python Kerberos Credential Cache Collection Utilities

%description -n python3-cccolutils
Python utilities for Kerberos Credential Cache Collections



%prep
%autosetup -n CCColUtils-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-cccolutils
%license COPYING
%{python3_sitearch}/cccolutils*.so
%{python3_sitearch}/CCColUtils-*.egg-info


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-11
- Subpackage python2-cccolutils has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-8
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5-2
- Rebuild for Python 3.6

* Mon Dec 12 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.5-1
- Update to 1.5 for EL6

* Wed Nov 30 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.4-1
- Rebase to 1.4

* Thu Nov 24 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2-1
- Update to not ship the test suite
- Review improvements

* Wed Nov 23 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1-2
- Update to follow guidelines

* Wed Nov 23 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1-1
- Initial packaging
