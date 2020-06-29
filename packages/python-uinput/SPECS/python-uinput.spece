

# No python3 on el6
%if 0%{?el6}
%global with_python3 0
%endif

Name:           python-uinput
Version:        0.10.1
Release:        26%{?dist}
Summary:        Pythonic API to the Linux uinput kernel module

License:        GPLv3
URL:            http://pypi.python.org/pypi/python-uinput/
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  kernel-headers
BuildRequires:  libudev-devel

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description\
Python-uinput is Python interface to the Linux uinput kernel module\
which allows attaching userspace device drivers into kernel.

%description %_description

%package -n     python3-uinput
Summary:        Pythonic API to the Linux uinput kernel module


%description -n python3-uinput
Python-uinput is Python interface to the Linux uinput kernel module
which
allows attaching userspace device drivers into kernel.


%prep
%setup -q -n %{name}-%{version}

# Use unversioned .so
sed -i "s/libudev.so.0/libudev.so/" setup.py

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py3_build


%install
%py3_install

chmod a-x examples/*


%files -n python3-uinput
%doc COPYING NEWS README examples
%{python3_sitearch}/python_uinput-%{version}-py?.?.egg-info
%{python3_sitearch}/_libsuinput.*.so
%{python3_sitearch}/uinput


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-26
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-24
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-23
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.1-20
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-18
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.1-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.1-15
- Python 2 binary package renamed to python2-uinput
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.1-12
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Mar 28 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.1-2
- Don't  build py3 on el6

* Fri Feb 28 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.10.1-1
- Update to latest upstram

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Fabian Deutsch <fabiand@fedoraproject.org> - 0.9-2
- Add documentation and examples

* Mon Nov 19 2012 Fabian Deutsch <fabian.deutsch@gmx.de> - 0.9-1
- Initial package.
