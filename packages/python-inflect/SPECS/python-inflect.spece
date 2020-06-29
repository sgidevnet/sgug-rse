%global srcname inflect
Name:           python-%{srcname}
Version:        2.1.0
Release:        7%{?dist}
Summary:        Correctly generate plurals, singular nouns, ordinals and indefinite articles

License:        MIT
URL:            https://github.com/jazzband/inflect
Source0:        %pypi_source

BuildArch:      noarch

%description
The methods of the class 'engine' in module 'inflect.py' provide plural
inflections, singular noun inflections, "a"/"an" selection for English words,
and manipulation of numbers as words.

Plural forms of all nouns, most verbs, and some adjectives are provided. Where
appropriate, "classical" variants (for example: "brother" -> "brethren",
"dogma" -> "dogmata", etc.) are also provided.

Single forms of nouns are also provided. The gender of singular pronouns can be
chosen (for example "they" -> "it" or "she" or "he" or "they").

Pronunciation-based "a"/"an" selection is provided for all English words, and
most initialisms.

It is also possible to inflect numerals (1,2,3) to ordinals (1st, 2nd, 3rd) and
to English words ("one", "two", "three").

%package -n python3-%{srcname}
Summary:        Correctly generate plurals, singular nouns, ordinals and indefinite articles
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

# Required for check
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-six

%description -n python3-%{srcname}
The methods of the class 'engine' in module 'inflect.py' provide plural
inflections, singular noun inflections, "a"/"an" selection for English words,
and manipulation of numbers as words.

Plural forms of all nouns, most verbs, and some adjectives are provided. Where
appropriate, "classical" variants (for example: "brother" -> "brethren",
"dogma" -> "dogmata", etc.) are also provided.

Single forms of nouns are also provided. The gender of singular pronouns can be
chosen (for example "they" -> "it" or "she" or "he" or "they").

Pronunciation-based "a"/"an" selection is provided for all English words, and
most initialisms.

It is also possible to inflect numerals (1,2,3) to ordinals (1st, 2nd, 3rd) and
to English words ("one", "two", "three).

%prep
%autosetup -n %{srcname}-%{version}
rm -rf inflect.egg-info

%build
%py3_build

%install
%py3_install

%check
pytest-3

%files -n python3-inflect
%license LICENSE
%doc CHANGES.txt README.rst
%{python3_sitelib}/inflect.py
%{python3_sitelib}/__pycache__/inflect.*.py*
%{python3_sitelib}/inflect-%{version}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 David Shea <dshea@redhat.com> - 2.1.0-1
- Update to 2.1.0
- Update license from AGPLv3+ to MIT
- Remove python2 subpackage

* Mon Jul 23 2018 David Shea <dshea@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.5-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.5-13
- Fix creation of python2- subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-10
- Rebuild for Python 3.6

* Wed Dec 21 2016 David Shea <dshea@redhat.com> - 0.2.5-10
- Use the more generic nosetests-3 now that it exists.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 David Shea <dshea@redhat.com> - 0.2.5-6
- Update %%check to use python 3.5
- Switched to the new packaging guidelines which renames python-inflect to python2-inflect

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 David Shea <dshea@redhat.com> - 0.2.5-3
- Change the build commands to not use py3dir external to the build directory
- Actually run the tests in %%check

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.2.5-2
- Use %%license for the license file

* Tue Jan 13 2015 David Shea <dshea@redhat.com> - 0.2.5-1
- Update to inflect-0.2.5, which fixes the following issues:
- Fixed TypeError while parsing compounds (by yavarhusain)
- Fixed encoding issue in setup.py on Python 3

* Mon Jul 21 2014 David Shea <dshea@redhat.com> - 0.2.4-4
- Separate the python2 and python3 buildrequires by package section

* Mon Jul 21 2014 David Shea <dshea@redhat.com> - 0.2.4-3
- Capitalize "English" in the description

* Tue Jul  8 2014 David Shea <dshea@redhat.com> - 0.2.4-2
- Remove rst markup from the description. Oops.

* Tue Jul  8 2014 David Shea <dshea@redhat.com> - 0.2.4-1
- Initial package
