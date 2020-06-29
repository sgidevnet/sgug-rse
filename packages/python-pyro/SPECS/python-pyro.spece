Name:           python-pyro 
Version:        4.71
Release:        11%{?dist}
Summary:        PYthon Remote Objects

License:        MIT 
URL:            http://packages.python.org/Pyro4/ 
Source0:        http://pypi.python.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: /usr/bin/2to3

%global _description\
Pyro provides an object-oriented form of RPC. You can use Pyro within a\
single system but also use it for IPC. For those that are familiar with\
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less\
similar to CORBA - which is a system- and language independent Distributed\
Object Technology and has much more to offer than Pyro or RMI.

%description %_description

%package -n python3-pyro
Summary:        Python Remote Objects
%description -n python3-pyro
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%prep
%setup -q -n Pyro4-%{version}

%build
%py3_build

%install
find examples -type f -exec sed -i 's/\r//' {} \;
find docs -type f -exec sed -i 's/\r//' {} \;
sed -i 's/\r//' LICENSE
chmod -x examples/echoserver/{Readme.txt,client.py}
chmod -x examples/gui_eventloop/{gui_threads.py,gui_nothreads.py}
chmod -x examples/maxsize/Readme.txt

%py3_install
find examples -type f -exec sed -i 's/\r//' {} \;
find docs -type f -exec sed -i 's/\r//' {} \;
sed -i 's/\r//' LICENSE
chmod -x examples/echoserver/{Readme.txt,client.py}
chmod -x examples/gui_eventloop/{gui_threads.py,gui_nothreads.py}
chmod -x examples/maxsize/Readme.txt

%files -n python3-pyro
%doc docs/* examples LICENSE
%{python3_sitelib}/Pyro4
%{python3_sitelib}/Pyro4-*.egg-info
%{_bindir}/pyro4*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.71-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.71-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.71-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.71-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.71-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.71-3
- Rebuilt for Python 3.7

* Fri Apr 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.71-2
- Package the executables only in python3-pyro

* Sun Apr 1 2018 David Hannequin <david.hannequin@gmail.com> 4.71-1
- Update from upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.14-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.14-14
- Python 2 binary package renamed to python2-pyro
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.14-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 David Hannequin <david.hannequin@gmail.com> 4.14-2
- adapt to el6

* Wed Aug 22 2012 David Hannequin <david.hannequin@gmail.com> 4.14-1
- Update from upstream
- Fix url 

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 4.9-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 1 2011 David Hannequin <david.hannequin@gmail.com> 4.9-1
- Update from upstream

* Wed Mar 13 2011 David Hannequin <david.hannequin@gmail.com> 4.3-2
- Python 3 support (thanks Haïkel Guémar)

* Sat Mar 9 2011 David Hannequin <david.hannequin@gmail.com> 4.3-1
- Update from upstream

* Sun Jan 16 2011 David Hannequin <david.hannequin@gmail.com> 4.2-1
- Update from upstream

* Tue Oct 12 2010 David Hannequin <david.hannequin@gmail.com> 4.0-3
- package for Fedora 13 

* Mon Oct 11 2010 David Hannequin <david.hannequin@gmail.com> 4.0-2
- Delete clean section
- Add license file

* Tue Aug 03 2010 David Hannequin <david.hannequin@gmail.com> 4.0-1
- First release to Fedora
