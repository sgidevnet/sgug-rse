Name:           python-pyeclib
Version:        1.5.0
Release:        14%{?dist}
Summary:        Python interface to erasure codes

License:        BSD
URL:            https://bitbucket.org/kmgreen2/pyeclib/
# We pull the tag using git CLI. Save the current command for Source0 below.
#  git archive -o ../pyeclib-1.5.0.tar.gz --prefix=pyeclib-1.5.0/ 1.5.0
Source0:        pyeclib-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  liberasurecode-devel >= 1.5.0

%global _description\
This library provides a simple Python interface for implementing erasure\
codes. A number of back-end implementations is supported either directly\
or through the C interface liberasurecode.

%description %_description

%package -n python3-pyeclib
Summary:        Python 3 interface to erasure codes

%description -n python3-pyeclib
This library provides a simple Python 3 interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%prep
%setup -q -n pyeclib-%{version}

%build
%py3_build

%install
%py3_install
 
%files -n python3-pyeclib
%license License.txt
%doc README.rst
%{python3_sitearch}/pyeclib*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0-3
- Python 2 binary package renamed to python2-pyeclib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Pete Zaitcev <zaitcev@redhat.com> 1.5.0-1
- Upstream 1.5.0, companion with liberasurecode 1.5.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuild for Python 3.6

* Thu Dec 08 2016 Pete Zaitcev <zaitcev@redhat.com> 1.4.0-1
- Upstream 1.4.0, companion with liberasurecode 1.4.0

* Wed Oct 19 2016 Pete Zaitcev <zaitcev@redhat.com> 1.3.1-1
- Update to upstream 1.3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 03 2016 Pete Zaitcev <zaitcev@redhat.com> 1.2.0-1
- Update to upstream 1.2.0: drop built-in liberasurecode

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 23 2015 Pete Zaitcev <zaitcev@redhat.com> 1.1.0-1
- Update to upstream 1.1.0

* Sun Oct 11 2015 Pete Zaitcev <zaitcev@redhat.com> 1.0.9-1
- Update to upstream 1.0.9
- Make py3 conditional for old system releases

* Tue Apr 21 2015 Pete Zaitcev <zaitcev@redhat.com> 1.0.7-2
- Correct the reported version from 1.0.5 to 1.0.7
- Address Haikel's comments (#1212148)
- Add BuildRequires: python-setuptools

* Wed Apr 15 2015 Pete Zaitcev <zaitcev@redhat.com> 1.0.7-1
- Update to upstream 1.0.7 (asked by Swift with EC and follow-up fixups)

* Thu Apr 02 2015 Pete Zaitcev <zaitcev@redhat.com> 1.0.6-1
- Initial release
