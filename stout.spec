%global debug_package %{nil}

%global commit c784a5efc2431babcb39a078f8b2af5b7bf5f0cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stout
Summary:        C++ headers for building sturdy software
Version:        0.1.1
Release:        5.%{shortcommit}%{?dist}

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/3rdparty/stout

## Will use this when pull-request in merged by upstream
#  https://github.com/3rdparty/stout/pull/4
#Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
#
#  We'll use this during devel :)
#
Source0:        https://github.com/besser82/stout/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%{?el5:BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildArch:      noarch

BuildRequires:  automake
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel

Provides:       %{name}-devel%{?isa} = %{version}-%{release}

Requires:       boost-devel%{?isa}
Requires:       protobuf-devel%{?isa}
## TBD - glog removed in the future
Requires:       glog-devel%{?isa}
Requires:       gmock-devel%{?isa}
Requires:       gtest-devel%{?isa}
Requires:       zlib-devel%{?isa}
Requires:       libcurl-devel%{?isa}

%description
Headers used for for development of sturdy applications, and leveraged
by Mesos.

Stout is a header only library that is contains a series of primitives
to assist in the development of building sturdy C++ applications.  Currently
this application is leveraged by Mesos.

Note: as that project has only headers (i.e., no library/binary object),
this package (i.e., the -devel package) is the one containing all of the
project.  There's no package with a library to link for this.


%prep
%setup -qn %{name}-%{commit}
cp -pr ./tests ./examples
rm -rf ./examples/*.a[cm]


%build
autoreconf -vfi
%configure
make %{?_smp_mflags}

%check
make check

%install
%if 0%{?el5}
  rm -rf %{buildroot}
  make install DESTDIR=%{buildroot}
%else
  %make_install
%endif


%clean
%{?el5:rm -rf %{buildroot}}


%files
%{_datadir}/pkgconfig/*
%{_includedir}/%{name}/
%doc LICENSE README examples


%changelog
* Tue Sep 3 2013 Timothy St. Clair <tstclair@redhat.com> 0.1.0-5.b1d3cc4d
- Minor update to the tip of mesos

* Fri Aug 16 2013 Timothy St. Clair <tstclair@redhat.com> 0.1.0-4.4e63c67
- Updating to the tip of mesos dated 8.15.2013

* Fri Aug  9 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.1-3.7c9d71c
- Update to latest

* Thu Jul 25 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-2.2d3d1ab
- use datadir instead of libdir for pkg-config
- make package noarch again

* Thu Jul 25 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-1.10f7b88
- new version
- ships a pkg-config-file now, must be arched now
- make install-target is supported
- adding test-dir as examples
- using autoreconf instead of bootstrap-script
- disable building debuginfo
- general clean-up and nuked trailing whitespaces
- added needs for el5
- changed %%define --> %%global
- dropped -devel-subpkg without main-pkg and make pkg provide -devel

* Mon Jul 22 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-1.270dba8
- In release added git shotcommit
- In BuildRequires added automake
- Droped BuildRoot target (since Fedora 18 was deprecated)
- Dropped %%clean section (since Fedora 18 was deprecated)
- Dropped %%defattr directives (since Fedora 18 was deprecated)
- Dropped %%files section (not needed)
- other fixes

* Mon Jul 22 2013 Timothy St. Clair <tstclair@redhat.com> 0.1.0-1
- initial fedora package
