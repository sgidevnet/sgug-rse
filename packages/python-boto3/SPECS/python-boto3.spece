%global pypi_name boto3

Name:           python-%{pypi_name}
Version:        1.14.12
Release:        1%{?dist}
Summary:        The AWS SDK for Python

License:        ASL 2.0
URL:            https://github.com/boto/boto3
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%package -n     python3-%{pypi_name}
Summary:        The AWS SDK for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove online tests
rm -rf tests/integration

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info/

%changelog
* Sat Jun 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.12-1
- 1.14.12

* Fri Jun 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.11-1
- 1.14.11

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.10-1
- 1.14.10

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.9-1
- 1.14.9

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.8-1
- 1.14.8

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.7-1
- 1.14.7

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.6-1
- 1.14.6

* Thu Jun 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.5-1
- 1.14.5

* Wed Jun 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.4-1
- 1.14.4

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.3-1
- 1.14.3

* Sat Jun 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.2-1
- 1.14.2

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.1-1
- 1.14.1

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.14.0-1
- 1.14.0

* Sat Jun 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.24-1
- 1.13.24

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.23-1
- 1.13.23

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.22-1
- 1.13.22

* Tue Jun 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.20-1
- 1.13.20

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.19-1
- 1.13.19

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.16-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.16-1
- 1.13.16

* Thu May 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.15-1
- 1.13.15

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.14-1
- 1.13.14

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.11-1
- 1.13.11

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.10-1
- 1.13.10

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.9-1
- 1.13.9

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.8-1
- 1.13.8

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.7-1
- 1.13.7

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.6-1
- 1.13.6

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.5-1
- 1.13.5

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.4-1
- 1.13.4

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.3-1
- 1.13.3

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.2-1
- 1.13.2

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.1-1
- 1.13.1

* Fri May 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.13.0-1
- 1.13.0

* Thu Apr 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.49-1
- 1.12.49

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.48-1
- 1.12.48

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.47-1
- 1.12.47

* Sat Apr 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.46-1
- 1.12.46

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.45-1
- 1.12.45

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.44-1
- 1.12.44

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.43-1
- 1.12.43

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.42-1
- 1.12.42

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.41-1
- 1.12.41

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.40-1
- 1.12.40

* Thu Apr 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.39-1
- 1.12.39

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.38-1
- 1.12.38

* Tue Apr 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.37-1
- 1.12.37

* Mon Apr 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.36-1
- 1.12.36

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.35-1
- 1.12.35

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.34-1
- 1.12.34

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.33-1
- 1.12.33

* Mon Mar 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.32-1
- 1.12.32

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.31-1
- 1.12.31

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.30-1
- 1.12.30

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.29-1
- 1.12.29

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.28-1
- 1.12.28

* Tue Mar 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.27-1
- 1.12.27

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.26-1
- 1.12.26

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.25-1
- 1.12.25

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.24-1
- 1.12.24

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.23-1
- 1.12.23

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.22-1
- 1.12.22

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.21-1
- 1.12.21

* Fri Mar 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.20-1
- 1.12.20

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.19-1
- 1.12.19

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.18-1
- 1.12.18

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.17-1
- 1.12.17

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.16-1
- 1.12.16

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.15-1
- 1.12.15

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.14-1
- 1.12.14

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.13-1
- 1 12.13

* Tue Mar 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.12-1
- 1.12.12

* Fri Feb 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.9-1
- 1.12.9

* Thu Feb 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.12.8-1
- Update to 1.12.8

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.7-1
- 1.12.7

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.6-1
- 1.12.6

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.5-1
- 1.12.5

* Fri Feb 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.4-1
- 1.12.4

* Thu Feb 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.12.3-1
- 1.12.3

* Wed Feb 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.11.17-1
- 1.11.17

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.11.12-1
- Update to 1.11.12

* Wed Jan 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.11.9-1
- Update to 1.11.9

* Fri Jan 17 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.11.4-1
- Update to 1.11.4 (rhbz#1677949)

* Mon Jan 13 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.11.0-1
- Update to 1.11.0 (rhbz#1677949)

* Wed Nov 20 2019 Orion Poplawski <orion@nwra.com> - 1.10.22-1
- Update to 1.10.21

* Mon Sep 09 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.9.225-1
- Update to 1.9.225 (rhbz#1677949)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.101-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.101-1
- Update to 1.9.101

* Fri Feb 15 2019 Kevin Fenzi <kevin@scrye.com> - 1.9.96-1
- Update to 1.9.96. Fixes bug #1667629

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.15-3
- Enable python dependency generator

* Thu Dec 20 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.15-2
- Subpackage python2-boto3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.9.15-1
- Update to 1.9.15

* Wed Jul 18 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1.7.41-1
- Upstream 1.7.41 (Fix compat with botocore 1.10.41)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 28 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.19-1
- Update to 1.5.19

* Sat Jan 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.18-1
- Update to 1.5.18

* Tue Jan 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.15-1
- Update to 1.5.15

* Wed Jan 10 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.12-1
- Update to 1.5.12

* Wed Jan 03 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.5.7-1
- Update to 1.5.7

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.6-1
- Update to 1.4.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.4-1
- Update to 1.4.4

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.3-1
- Update to 1.4.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuild for Python 3.6

* Sat Dec 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> 1.4.2-1
- Update to 1.4.2

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.4.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.1-1
- New upstream release

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.3.0-1
- New upstream release

* Fri Feb 19 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.4-1
- New upstream release

* Thu Feb 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.3-3
- Fix python2- subpackage to require python-future

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.2.3-1
- Initial package.
