%global pypi_name pytest-mock
%global file_name pytest_mock
%global desc This plugin installs a mocker fixture which is a thin-wrapper around the \
patching API provided by the mock package, but with the benefit of not having \
to worry about undoing patches at the end of a test.


Name:           python-%{pypi_name}
Version:        1.10.4
Release:        9%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-mock
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-mock/pytest-mock-%{version}.tar.gz
BuildArch:      noarch
# Fix tests expectations with latest pytest (4.6.3+)
Patch0:         fix-expectations-pytest-4.6.3.patch
# Fix tests due to new formatting in mock 3.0 and python 3.8 (See https://github.com/pytest-dev/pytest-mock/commit/b3badafebedea3605c90eb22a68adff2885a8bb0)
Patch1:         fix-mock-python-3.8.patch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
BuildRequires:  python3-setuptools_scm
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info
%patch0 -p1
%patch1 -p1

# Correct end of line encoding for README
sed -i 's/\r$//' README.rst


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="$(pwd)" py.test-%{python3_version} test_pytest_mock.py


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}.py*
%{python3_sitelib}/__pycache__/%{file_name}*.py*
%{python3_sitelib}/_pytest_mock_version.py*
%{python3_sitelib}/__pycache__/_pytest_mock_version.cpython*


%changelog
* Fri May 29 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-9
- Drop manual requires on python3-pytest to support usage with pytest4 compat package

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-6
- Subpackage python2-pytest-mock has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-5
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Julien Enselme <jujens@jujens.eu> - 1.10.4-4
- Fix build issues with python 3.8 and mock 3.0

* Tue Jul 30 2019 Julien Enselme <jujens@jujens.eu> - 1.10.4-3
- Fix build issues with pytest 4.6.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 1.10.4-1
- Update to 1.10.4

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.3-1
- Update to 1.10.3

* Sat Feb 23 2019 Julien Enselme <jujens@jujens.eu> - 1.10.1-1
- Update to 1.10.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Mon May 07 2018 Julien Enselme <jujens@jujens.eu> - 1.10.0-1
- Update to 1.10.0

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 1.9.0-1
- Update to 1.9.0

* Thu Mar 01 2018 Julien Enselme <jujens@jujens.eu> - 1.7.1-1
- Update to 1.7.1

* Mon Feb 19 2018 Julien Enselme <jujens@jujesn.eu> - 1.7.0-1
- Update to 1.7.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Julien Enselme <jujens@jujens.eu> - 1.6.3-1
- Update to 1.6.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Julien Enselme <jujens@jujens.eu> - 1.6.2-1
- Update to 1.6.2

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-2
- Add missing BR

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 1.6.0-1
- Update to 1.6.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-3
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 1.2-2
- Add patch to fix tests with pytest3

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 1.2-1
- Update to 1.2

* Wed Aug 31 2016 Julien Enselme <jujens@jujens.eu> - 1.1-3
- Use %%summary instead of custom %%sum macro

* Mon Aug 29 2016 Julien Enselme <jujens@jujens.eu> - 1.1-2
- Add python2-mock to BR so %%check passes correctly.

* Tue Jul 26 2016 Julien Enselme <jujens@jujens.eu> - 1.1-1
- Inital package
