Name:           pss
Version:        1.40
Release:        14%{?dist}
Summary:        A power-tool for searching inside source code files

License:        Public Domain
URL:            https://github.com/eliben/pss
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel, python3-setuptools
BuildArch:      noarch


%description
pss is a power-tool for searching inside source code files. 
pss searches recursively within a directory tree, knows which 
extensions and file names to search and which to ignore, automatically 
skips directories you wouldn't want to search in (for example .svn or .git),
colors its output in a helpful way, and does much more.


%prep
%setup -q


%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1  --root $RPM_BUILD_ROOT
#rm $RPM_BUILD_ROOT/usr/bin/pss.py


%files
%doc README.rst LICENSE CHANGES
%{_bindir}/pss
%{python3_sitelib}/pss*



%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.40-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.40-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Kushal Das <kushal@fedoraprojects.org> 1.40-2
- Python3 build command

* Thu Apr 09 2015 Kushal Das <kushal@fedoraprojects.org> 1.40-1
- New release of the tool on Python3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 1.38-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Wed Aug 28 2013 Kushal Das <kushal@fedoraprojects.org> 1.38-1
- new release of the tool

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Dec 19 2012 Kushal Das <kushal@fedoraprojects.org> 0.35-3
- removing few macros

* Fri Dec 14 2012 Kushal Das <kushal@fedoraprojects.org> 0.35-2
- updated based on suggestions in review request

* Mon Nov 19 2012 Kushal Das <kushal@fedoraprojects.org> 0.35-1
- Initial package creation
