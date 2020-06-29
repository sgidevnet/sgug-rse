# Created by pyp2rpm-3.3.0
%global pypi_name gitlab

Name:           python-%{pypi_name}
Version:        1.15.0
Release:        3%{?dist}
Summary:        Interact with GitLab API

License:        LGPLv3
URL:            https://github.com/python-gitlab/python-gitlab
Source0:        https://files.pythonhosted.org/packages/source/p/python-gitlab/python-gitlab-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(requests) >= 1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(httmock)
BuildRequires:  python3dist(mock)

%description
Interact with GitLab API

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Interact with GitLab API

%package -n python-%{pypi_name}-doc
Summary:        Python gitlab documentation
%description -n python-%{pypi_name}-doc
Documentation for gitlab

%prep
%autosetup -n python-%{pypi_name}-%{version}
for Files in gitlab/v4/cli.py gitlab/cli.py \
             gitlab/tests/test_cli.py ; do
  %{__sed} -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  %{__rm} ${Files}.orig
done

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{_bindir}/gitlab
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_gitlab-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%license COPYING
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Steve Traylen <steve.traylen@cern.ch> - 1.15.0-1
- New 1.15.0 version

* Mon Dec 16 2019 Steve Traylen <steve.traylen@cern.ch> - 1.14.0-1
- New 1.14.0 version

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 1.13.0-1
- New 1.13.0 version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Drop redundant runtime dependencies specified for auto-generated ones

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Subpackage python2-gitlab has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.7

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-3
- Correct copy paste error.

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-2
- Specify COPYING file. Add BR on python-mock.

* Fri May 11 2018 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-1
- Initial package.
