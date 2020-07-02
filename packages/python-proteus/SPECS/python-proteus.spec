%global major 4.0
%global module_name proteus

Name:           python-%{module_name}
Version:        4.0.2
Release:        13%{?dist}
Summary:        Library to access Tryton's internal objects

License:        GPLv3+
URL:            http://www.tryton.org
Source0:        http://downloads.tryton.org/%{major}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# needed for tests
#BuildRequires:  trytond-sqlite

Requires:       tryton(kernel) = %{major}


%description
A client library to access Tryton's internal objects like Models and Wizards.


%prep
%setup -q -n %{module_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
#%{__python3} setup.py test


%files
%doc CHANGELOG COPYRIGHT INSTALL LICENSE README
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/%{module_name}-%{version}-*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-2
- Rebuild for Python 3.6

* Fri Sep 09 2016 Dan Horák <dan@danny.cz> - 4.0.2-1
- new upstream version 4.0.2

* Wed Jul 27 2016 Dan Horák <dan@danny.cz> - 4.0.0-1
- new upstream version 4.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Dan Horák <dan@danny.cz> - 2.6.1-1
- new upstream version 2.6.1

* Sat Oct 27 2012 Dan Horák <dan@danny.cz> - 2.6.0-1
- new upstream version 2.6.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Dan Horák <dan@danny.cz> - 2.4.0-1
- new upstream version 2.4.0

* Sun Jan 15 2012 Dan Horák <dan@danny.cz> - 2.2.1-1
- new upstream version 2.2.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 2.0.0-1
- new upstream version 2.0.0

* Mon Feb 21 2011 Dan Horák <dan[at]danny.cz> - 1.8.1-1
- updated to 1.8.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Dan Horák <dan[at]danny.cz> - 1.8.0-2
- little update before submitting to review

* Fri Dec 31 2010 Dan Horák <dan[at]danny.cz> 1.8.0-1
- initial Fedora version
