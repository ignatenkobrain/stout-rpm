%global debug_package %{nil}

%global commit 10f7b887a96f1bbcc64c9e14f9450c427b0de83e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stout
Summary:        C++ headers for building sturdy software
Version:        0.1.1
Release:        1.%{shortcommit}%{?dist}

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/3rdparty/stout

## Will use this when pull-request in merged by upstream
#  https://github.com/3rdparty/stout/pull/4
#Source0:        https://github.com/3rdparty/stout/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
#
#  We'll use this during devel :)
Source0:        https://github.com/besser82/stout/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

## pkg-config-file forces arched pkg
#BuildArch:      noarch

BuildRequires:  automake, autoconf

%description
Stout is a header only library that is contains a series of primitives 
to assist in the development of building sturdy C++ applications.  Currently
this application is leveraged by Mesos.


%package devel
Summary:        C++ headers for building sturdy software
Group:          Development/Libraries
Provides:       %{name}%{?isa} = %{version}-%{release}
## This is superflous and useless, isn't it?
#Requires:       %{name}%{?isa} = %{version}-%{release}
Requires:       boost-devel%{?isa}
Requires:       protobuf-devel%{?isa}
## TBD - glog removed in the future
Requires:       glog-devel%{?isa}
Requires:       gmock-devel%{?isa}
Requires:       gtest-devel%{?isa}

%description devel
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


%build
autoreconf -vfi
%configure
make %{?_smp_mflags} 


%install
rm -rf %{buildroot}
%make_install
cp -pr ./tests ./examples


%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}/
%doc LICENSE README.md examples


%changelog
* Thu Jul 25 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-1.10f7b88
- new version
- ships a pkg-config-file now
- make install-target is supported
- adding test-dir as examples
- using autoreconf instead of bootstrap-script
- disable building debuginfo

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
