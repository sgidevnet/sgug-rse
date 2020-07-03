%global pypi_name boto3

Name:           python-%{pypi_name}
Version:        1.11.17
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
* Sun May 3 2020 Daniel Hams <daniel.hams@gmail.com> - 1.11.17-1
- Import into wip

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
